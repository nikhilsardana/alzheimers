# Nikhil Sardana, 7/21/17
######################################
# Write commands for unzipping
# 4d nii gz files.
#########################################

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

classes = ["ad", "emci", "lmci", "normal", "smc"]
q = open("extract_4d.txt", "w")
for myclass in classes:
    with open(myclass + ".txt") as f:
        filenames = f.readlines()

    for k in range(len(filenames)):
        if(k%2==0):     #odd lines contain structural MRI files
            fmri_dir = filenames[k].strip()
            fmri_file = fmri_dir + "/" + "4d.nii.gz"
            q.write("gzip -d " + fmri_file + "\n")


q.close()
