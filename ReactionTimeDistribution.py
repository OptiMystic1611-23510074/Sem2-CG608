import math
import pandas as pd
import matplotlib.pyplot as plt

def calculate_averages(data, coherence_delta_column, threshold, response_time_column):

  low_sum, high_sum, low_count, high_count = 0, 0, 0, 0

  for index, row in data.iterrows():
    if math.isnan(float(row[response_time_column])):
      continue
    value = abs(row[coherence_delta_column])  # Get absolute value
    if value <= threshold:
      low_sum += float(row[response_time_column])
      low_count += 1
    else:
      high_sum += float(row[response_time_column])
      high_count += 1

  low_average = low_sum / low_count if low_count > 0 else None  # Handle cases with no values in a category
  high_average = high_sum / high_count if high_count > 0 else None

  return [round(low_average,5), round(high_average,5)]


def print_results(results, val):
  #results [sub2-33][run0-1-2][low0-high1]
  for i in range(len(subs)):
    for j in range(3):
      for k in range(2):
        if k == 0:
          print(f'{subs[i]}-->run-0{j}-->low_{val}:  ', results[i][j][k])
        else:
          print(f'{subs[i]}-->run-0{j}-->high_{val}: ', results[i][j][k])
    print()

def plot_results_violinplot(results, cat, task):

  low = [item[0] for sublist in results for item in sublist]
  high = [item[1] for sublist in results for item in sublist]
  
  plt.violinplot([low, high])  # Remove labels argument
  plt.title(f"Reaction Time Distribution for \n{task}")
  plt.xlabel("Category")
  plt.ylabel("Reaction Time (ms)")
  plt.xticks([1, 2], [f"low_{cat}", f"high_{cat}"])  # Set custom x-axis labels and positions
  plt.show()


def plot_results_boxplot(results, cat, task):

  low = [item[0] for sublist in results for item in sublist]
  high = [item[1] for sublist in results for item in sublist]
  
  plt.boxplot([low, high])  # Remove labels argument
  plt.title(f"Reaction Time Distribution for \n{task}")
  plt.xlabel("Category")
  plt.ylabel("Reaction Time (ms)")
  plt.xticks([1, 2], [f"low_{cat}", f"high_{cat}"])
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.tight_layout()
  plt.show()
  

# Defining file paths

path = "E:\\Dataset\\ValueBasedDecision\\ds002006"
subpath = "func"
subs = [f"sub-{i:02}" for i in range(2, 34)]
#print(len(subs))
#sub = "sub-02"

color_dots_files = [
  "task-ColorDots_run-01_events.tsv",
  "task-ColorDots_run-02_events.tsv",
  "task-ColorDots_run-03_events.tsv"
]

food_choice_files = [
  "task-FoodChoice_run-01_events.tsv",
  "task-FoodChoice_run-02_events.tsv",
  "task-FoodChoice_run-03_events.tsv"
]

#print(f"{path}\\{sub}\\{subpath}\\{sub}_{color_dots_files}")
#print(f"{path}\\{sub}\\{subpath}\\{sub}_{food_choice_files}")

color_dots_results = []
color_dots_sub = []
food_choice_results = []
food_choice_sub = []

# Process ColorDots files
for sub in subs:
  for filename in color_dots_files:
    try:
      data = pd.read_csv(f"{path}\\{sub}\\{subpath}\\{sub}_{filename}", sep="\t")
      color_dots_sub.append(calculate_averages(data, "COHERENCE", 0.25, "RESPONSE_TIME"))
    except FileNotFoundError:
        pass
  color_dots_results.append(color_dots_sub)


#print_results(color_dots_results, 'coherence')
plot_results_violinplot(color_dots_results, 'coherence', 'Perceptual Decision Making Task (ColorDots)')
#plot_results_boxplot(color_dots_results, 'coherence', 'Perceptual Decision Making Task (ColorDots)')


# Process FoodChoice files
for sub in subs:
  for filename in food_choice_files:
    try:
      data = pd.read_csv(f"{path}\\{sub}\\{subpath}\\{sub}_{filename}", sep="\t")
      food_choice_sub.append(calculate_averages(data, "DELTAVALUE", 0.05, "RESPONSE_TIME"))
    except FileNotFoundError:
        pass
  food_choice_results.append(food_choice_sub)


#print_results(food_choice_results, 'delta')
plot_results_violinplot(food_choice_results, 'delta', 'Value-Based Decision Making Task (FoodChoice)')
#plot_results_boxplot(food_choice_results, 'delta', 'Value-Based Decision Making Task (FoodChoice)')


