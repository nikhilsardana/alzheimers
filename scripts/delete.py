#Nikhil Sardana
#8/19/17
#create deletion commands for preprocessed files

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

classes = ["ad", "emci", "lmci", "normal", "smc"]

cp = open("delete.txt", "w")

for myclass in classes:
    with open(myclass + "140" + ".txt") as f:
        filenames = f.readlines()

    for k in filenames:
        k = k.strip()
        if "Resting_State_fMRI" in k:
            cp.write("rm -rf " + k + "/4d_preprocessed.feat" + "\n")

cp.close()
