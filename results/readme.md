Since the CNN was trained on 2D slices, but fMRI data is 4D (3D brain scans over time), this folder contains various scripts to aggregate the network output.

First, we record network predictions for each of the 2D slices and then assign the 3D MRI to the category with the plurality of predictions. 
We then compare this prediction with the ground truth of the 3D file to calculate classification metrics.
Similarly, we calculate subject-level (4D) classification metrics by aggregating network predictions for all 2D slices over all time steps per subject.
