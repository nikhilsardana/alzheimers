#File transfer script.
#remove some files from the source
#and place in destination
import os
import shutil


src = "adsample/"
dest = "adcorrect/"

with open("mypredictions.csv") as f:
	j = f.readlines()

j = [x.strip() for x in j]
j = [x.strip('\n') for x in j]
quincy = [x.split(',') for x in j]
print(quincy)
print([x[0] for x in quincy])
print([x[1] for x in quincy])
#print([x[2] for x in quincy])
k=0
for x in quincy:
	if int(x[1])==int(x[0]):
		k+=1
		shutil.copyfile(src+x[2], dest+x[2])		
print(k)
