#Randomly choose a 2d slice in the middle
#for visualization.
#Slices on either end tend to contain little information.

import os
import random
import shutil
src = "imgdata/test/ad/"
dest = "weights/visualize/adsample/"
k = os.listdir("imgdata/test/ad/")
middle = []
for filename in k:
	twoparts = filename.split("-slice")[1]
	number = twoparts.split(".")[0]
	print(number)
	if(int(number)<37 and int(number)>13):
		middle.append(filename)

#print(middle)
j = random.sample(middle, 500)
f = open("adlist.txt", "w")
for myfile in j:
	f.write(myfile + "\n")
	shutil.copy(src+myfile, dest+myfile)

f.close()
