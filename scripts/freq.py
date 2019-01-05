#Nikhil Sardana
#8/19/17
#Create frequency list of each class
#Based on number of time-steps per 4d data-point (ie number of 3d files)

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

classes = ["ad", "emci", "lmci", "normal", "smc"]



for myclass in classes:
    with open(myclass + ".txt") as f:
        filenames = f.readlines()

    freq = {}
    for k in range(len(filenames)):
        if(k%2==0):                                                 #even lines contain all fmri folders
            fmri_dir = filenames[k].strip()
            fmri_list = os.listdir(fmri_dir)
            llist = [x for x in fmri_list if ".nii" in x]
            llen = len(llist)
            llen = llen - 1
            if (str(llen) in freq):
                freq[str(llen)] = freq[str(llen)] + 1
            else:
                freq[str(llen)] = 1
    print(freq)


