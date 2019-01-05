#Nikhil Sardana
#9/23

#nifi (.nii) to .npy
#for input into 3d-cnn
import os
import numpy as np
import nibabel

home_dir = "/home/nikhil/Documents/fmri/data/"

data = ["train", "test"]
classes = ["ad", "emci", "lmci", "normal", "smc"]

for datum in data:
	for myclass in classes:
		file_list = os.listdir(datum + "/" + myclass + "/")
		print(file_list)
