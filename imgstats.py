import cv2
import numpy as np
import math
import os
from random import shuffle
home_dir = "../imgdata/"
datatype = ["train", "test"]
classes = ["ad", "emci", "lmci", "normal", "smc"]

total=0.0
average = 0.0
values = []
fulldata = []
for datum in datatype:
    for cls in classes:
        folder = home_dir + "/" + datum + "/" + cls
        k = os.listdir(folder)
        shuffle(k)
        for img in k:
            j = folder + "/" + img
            calc = cv2.imread(j)
            fulldata.append(calc)
            average_color_per_row = np.average(calc, axis=0)
            average_color = np.average(average_color_per_row, axis=0)
            values.append(average_color[0]) #grayscale images mean avg_color[0]=avg_color[1]=avg_color[2]
            
            total += average_color[0]
            average = total/len(values)

            #printing
            if(len(values)%1000==0):
                print(len(values))
                print(average)
                i=0
                sumdiff=0.0
                for imagearray in fulldata:
                    flatimg = imagearray.flatten()
                    diff = [(pixel-average)*(pixel-average) for pixel in flatimg]
                    i+=len(flatimg) # counts every pixel in every image
                    sumdiff += sum(diff)
                standard_dev = math.sqrt(sumdiff/(i*1.00))
                print(standard_dev)
