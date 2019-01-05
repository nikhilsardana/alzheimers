#Nikhil Sardana
#8/19/17
# For the "problem" folders,
# Merge 3D Files into 4D file

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

folders = ['/home/nikhil/Documents/fmri/adni_nii/lmci/subj/006_S_4515/Resting_State_fMRI/2012-02-07_10_58_41.0/S140018',        #worked
            '/home/nikhil/Documents/fmri/adni_nii/lmci/subj/031_S_4721/Resting_State_fMRI/2013-05-23_14_52_19.0/S190432',       #worked
            '/home/nikhil/Documents/fmri/adni_nii/normal/subj/012_S_4026/Resting_State_fMRI/2011-12-07_10_02_11.0/S134859',     #didnt work
            '/home/nikhil/Documents/fmri/adni_nii/normal/subj/002_S_4225/Resting_State_fMRI/2011-09-21_10_07_24.0/S122882',     #worked
            '/home/nikhil/Documents/fmri/adni_nii/normal/subj/013_S_4579/Resting_State_fMRI/2012-04-04_18_01_24.0/S146811',     #worked
            '/home/nikhil/Documents/fmri/adni_nii/normal/subj/006_S_4485/Resting_State_fMRI/2012-08-24_11_45_03.0/S162595',     #didn't work
            '/home/nikhil/Documents/fmri/adni_nii/normal/subj/002_S_0685/Resting_State_fMRI/2012-07-27_09_17_54.0/S160105']     #worked

mcommand = open("merge2.txt", "w")

for fmri_dir in folders:
    fmri_list = os.listdir(fmri_dir)                        #list all fmri timesteps
    no_ext_list = [x.split(".")[0] for x in fmri_list]      #remove extensions
    full_list = [fmri_dir + "/" + x for x in no_ext_list]   #add in full path

    full_list.sort()
    commnd = "fslmerge -t " + fmri_dir + "/" + "4d" + " " #merge command


    for q in full_list:
        commnd += q
        commnd += " "

    mcommand.write(commnd+"\n")   #write merge command

mcommand.close()
