#Nikhil Sardana
#11/8/17

filename = "twodresults.csv"
with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content] 

matrix = [x.split(',') for x in content]

filestem = [x[2].split('-')[0] for x in matrix]

uniquestems = set(filestem)
freqlist = [[0,0,0,0,0,0] for x in range(len(uniquestems))]

i=0
for threedstem in uniquestems:
	if("ad" in threedstem):
		freqlist[i][5] = 0
	elif("emci" in threedstem):
		freqlist[i][5] = 1
	elif("lmci" in threedstem):
		freqlist[i][5] = 2
	elif("normal" in threedstem):
		freqlist[i][5] = 3
	elif("smc" in threedstem):
		freqlist[i][5] = 4
	else:
		print("Something's gone wrong!")
		print(threedstem)
		quit()
	for twodslice in matrix:
		if threedstem in twodslice[2]:
			freqlist[i][int(twodslice[0])] += 1
	i+=1
	print(i)
print(freqlist)

instances = [0,0,0,0,0]
correct = [0,0,0,0,0]
incorrect = [0,0,0,0,0]
for q in freqlist:
	j = q[0:5]
	instances[q[5]]+=1	#another ad (or emci, lmci, etc.) subject in the dataset
	if j.index(max(j)) == q[5]:
		correct[q[5]]+=1
	else:
		incorrect[q[5]]+=1

print(instances)
print(correct)
print(incorrect)
print(sum(correct)/sum(instances))
