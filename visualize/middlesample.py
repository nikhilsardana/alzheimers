#sample a middle slice from one of the 
#correctly classified alzheimer's brains.

import os
import random
import shutil
src = "adcorrect/ad/"
dest = "admiddle/ad/"
k = os.listdir(src)
middle = []
j = []
for filename in k:
	subj = int(filename.split("_")[2])
	twoparts = filename.split("-slice")[1]
	number = twoparts.split(".")[0]
	print(number)
	hash = subj*1000 + int(number)
	if not hash in j:
		j.append(hash)
		if(int(number)<37 and int(number)>24):
			middle.append(filename)


j = random.sample(middle, 100)
f = open("adlist.txt", "w")
for myfile in j:
	f.write(myfile + "\n")
	shutil.copy(src+myfile, dest+myfile)

f.close()
