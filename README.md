# Sem2-CG608
## Neuroscience of Decision Making

#### This repository has coursework material that was used for the course project.

<br />

----

In this project, I have tried to replicate the results obtained for experiment 1 from the study by Bakkour et al. ([2019](https://doi.org/10.7554/elife.46080)), specifically the value-based decision making and the perceptual decision-making tasks by healthy individuals. It suggests that hippocampus plays role in value-based decisions and helps us imagine possible outcomes in future and compare options. This was a functional magnetic resonance imaging (fMRI) study in which value-based (food choice) and perceptual (colour dots) decision making tasks were done by normal and amnesic participants.

I have focused to understand any patterns between effects of internal and external pieces of evidence. The healthy participants dataset was available on OpenNeuro (Bakkour et al., [2019](https://doi.org/10.18112/openneuro.ds002006.v1.0.1)). The conditions were derived based on the events.tsv files (discussed under the methods section). First, preprocessing was done, then model was fitted into a general linear model in first level analysis. The implications of the results obtained were discussed and found to be consistent with the original study.

First, reaction time plots were created for all subjects using Python. It could be seen that low differences (low_coherence and low_delta) demands for more time to deliberate as compared to high differences (high_coherence and high_delta). As per these plots, it seems for the perceptual decision-making task this the RT difference is more. But the difference can also be seen for the Value-Based decision-making task. This is consistent with what has been reported in the original study. The delta values are not spread across a wide range like the colour coherence values. Furthermore, the reaction time values are also not widespread for the value-based decision-making task as compared to the perceptual decision-making task.
Script: https://github.com/OptiMystic1611-23510074/Sem2-CG608/blob/main/scripts/ReactionTimeDistribution.py*

Next, I did Statistical Parametric Mapping on the fMRI recordings using SPM toolkit in MATLAB, by following all the standard preprocessing steps and proceeded to do first level analysis. Contrasts were defined on the model to asses the level of activation in different conditions. A low_delta vs high_delta value brain plots obtained by a contrast defined as -0.5 for high_delta condition and +0.5 for low_delta condition for all three sessions [-0.5 0.5 -0.5 0.5 -0.5 0.5]. BOLD activity was seen around the hippocampus and medial-temporal (MT) regions. A p-value of 0.05 and voxel extension value of 10 was set. The obtained results were found to be consistent with the original study. Though the activations obtained are more towards the MT lobe and less towards the hippocampus in this project. It is important to note that the plot is obtained by just first level analysis, whereas in the original study the final results are obtained with a conjunction analysis. 


----

<br />

Please note that the dataset used for this project is not owned by me.

**Original Authors:** Akram Bakkour, Daphna Shohamy, Michael N. Shadlen

**OpenNeuro URL:** https://openneuro.org/datasets/ds002006/versions/1.0.1
