#Nikhil Sardana
#8/21/17
#Split files into lists based on number of time-steps
#140 timesteps, 280 timesteps, and other timesteps
#this is because FEAT analysis requires the same number of time-steps per 4d file

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

classes = ["ad", "emci", "lmci", "normal", "smc"]

for myclass in classes:
    with open(myclass + ".txt") as f:
        filenames = f.readlines()
    
    g = open(myclass + "140.txt", "w")
    h = open(myclass + "280.txt", "w")
    i = open(myclass + "_other.txt", "w")

    freq = {}
    for k in range(len(filenames)):
        if(k%2==0):                                                 #even lines contain all fmri folders
            fmri_dir = filenames[k].strip()
            fmri_list = os.listdir(fmri_dir)
            llist = [x for x in fmri_list if ".nii" in x]
            llen = len(llist)
            llen = llen - 1
            if(llen==140):
                g.write(fmri_dir + "\n")
                g.write(filenames[k+1].strip() + "\n")
            if(llen==280):
                h.write(fmri_dir + "\n")
                h.write(filenames[k+1].strip() + "\n")
            else:
                i.write(fmri_dir + "\n")
                i.write(filenames[k+1].strip() + "\n")


g.close()
h.close()
i.close()

