#Nikhil Sardana
#8/19/17
#create copy commands for preprocessed files

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

classes = ["ad", "emci", "lmci", "normal", "smc"]

#####
#randomly chosen testing data (3:1 split)
#chosen by np.random.choice(total_files, number_of_testing_files, replace=False)
#        Training  Testing   Ratio
#ad          65      21      3.095
#emci        92      30      3.066       
#lmci        76      25      3.040
#normal      54      18      3.000
#smc         27      9       3.000
#####
ad = [18, 79, 49, 41, 47, 68,  0, 83, 29, 16, 37, 73, 21, 78, 66, 45, 36,
       76,  1,  6, 22]
emci = [4, 110, 101,  19,  12,  29, 100,  62,  54,  86,  90,  30,  87,
        74,  37,  49,  52,  55, 121,  72,  38,  47,  14,  80,  23,  27,
       117,  68,  73, 115]
lmci = [95, 39, 32, 25, 49, 89,  5, 44, 87, 93,  8, 48, 98, 63,  3, 66,  0,
       91, 74, 72, 31, 96, 37, 82, 29]
normal = [4, 64, 14, 42, 19,  9, 27, 35, 37, 23, 57, 49, 56, 70,  6, 58, 60,45]
smc = [13, 25, 23,  3, 16,  1, 33,  9, 15]

class_data = [ad, emci, lmci, normal, smc]

cp = open("copy.txt", "w")

j = 0
for myclass in classes:
    with open(myclass + "140" + ".txt") as f:
        filenames = f.readlines()
    i = 0
    for k in filenames:
        k = k.strip()
        if "Resting_State_fMRI" in k:
            if i in class_data[j]:
                keyword = "test"
            else:
                keyword = "train"

            cp.write("mkdir data/" + keyword + "/" + myclass + "/subj_" + str(i) + "\n")
            cp.write("cp " + k + "/4d_preprocessed.feat/filtered_func_data.nii.gz" + " " + "data/" + keyword + "/" + myclass + "/subj_" + str(i) + "\n")
            
            i = i+1
    j = j+1
cp.close()
