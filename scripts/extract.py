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
for myclass in classes:
    with open(myclass + ".txt") as f:
        filenames = f.readlines()

    for k in range(len(filenames)):
        if(k%2==1):     #odd lines contain structural MRI files
            struct_dir = filenames[k].strip()
            struct_list = os.listdir(struct_dir)
            g = [x for x in struct_list if ".gz" in x]
            #if(len(g)==1):
            #    wo_ext = struct_dir + "/" + g[0]
            #    q.write("gzip -d " + wo_ext + "\n")
            if(len(g)!=0):
                print('ayy')


