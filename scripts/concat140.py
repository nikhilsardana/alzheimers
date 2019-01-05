#Nikhil Sardana
#8/19/17
#Merge 3D Files into 4D file

from glob import glob
import os

home_dir = "/home/nikhil/Documents/fmri/adni_nii/"

classes = ["ad", "emci", "lmci", "normal", "smc"]


rs = open("rs140.txt", "w")
struct = open("struct140.txt", "w")

for myclass in classes:
    with open(myclass + "140" + ".txt") as f:
        filenames = f.readlines()

    for k in filenames:
        k = k.strip()
        if "Resting_State_fMRI" in k:
            rs.write(k + "/4d.nii" + "\n")
        else:
            struct_dir = k
            struct_list = os.listdir(struct_dir)
            g = [x for x in struct_list if "brain" in x]
            w_ext = struct_dir + "/" + g[0]
            struct.write(w_ext + "\n")


rs.close()
struct.close()