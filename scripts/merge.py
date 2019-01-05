#Nikhil Sardana
#8/19/17
#Merge 3D Files into 4D file

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

classes = ["ad", "emci", "lmci", "normal", "smc"]

mcommand = open("mergecomm.txt", "w")

for myclass in classes:
    gg = open(myclass + "2" + ".txt", 'w')
    with open(myclass + ".txt") as f:
        filenames = f.readlines()

    for k in range(len(filenames)):
        if(k%2==0):                                                 #even lines contain all fmri folders
            fmri_dir = filenames[k].strip()
            fmri_list = os.listdir(fmri_dir)                        #list all fmri timesteps
            no_ext_list = [x.split(".")[0] for x in fmri_list]      #remove extensions
            full_list = [fmri_dir + "/" + x for x in no_ext_list]   #add in full path

            full_list.sort()
            commnd = "fslmerge -t " + fmri_dir + "/" + "4d" + " " #merge command

            gg.write(fmri_dir + "/" + "4d.nii" + "\n")
            gg.write(filenames[k+1].strip() + "\n")

            for q in full_list:
                commnd += q
                commnd += " "

            mcommand.write(commnd+"\n")   #write merge command


    gg.close()

mcommand.close()
