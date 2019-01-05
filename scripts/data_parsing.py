# Nikhil Sardana, 7/21/17
######################################
# Data Parsing : Read Data from ADNI Files on external directory
# Write a list of the directories of fMRI data + corresponding structural MRI file
# Used before MATLAB Batch Pre-Processing
# Note: Highly specific. Relies of the structure of the ADNI data and folders
#########################################

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

classes = ["ad", "emci", "lmci", "normal", "smc"]
q = open("files.txt", "w")
for myclass in classes:
    with open(myclass + ".txt") as f:
        filenames = f.readlines()

    for k in range(len(filenames)):
        if(k%2==1):     #odd lines contain structural MRI files
            struct_dir = filenames[k].strip()
            struct_list = os.listdir(struct_dir)
            wo_ext = struct_list[0].split(".")[0]
            wo_new = wo_ext + "_brain"
            old_file = struct_dir + "/" + wo_ext
            new_file = struct_dir + "/" + wo_new    
            q.write("bet " + old_file + " " + new_file + "\n")

q.close()


