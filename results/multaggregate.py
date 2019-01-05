#Nikhil Sardana
#11/8/17
# O(n) time
# **********************************
# Commented lines for 3D Aggregation
# **********************************

def freqlist(filename):
	with open(filename) as f:
	    content = f.readlines()

	content = [x.strip() for x in content] 

	matrix = [x.split(',') for x in content]

	#filestem = [x[2].split('-')[0] for x in matrix]	#for 3d
	filestem = [x[2].split('slice_')[0] for x in matrix]	#for 4d
	
	uniquestems = set(filestem)
	print(len(uniquestems))
	#freqlist = [[0,0,0,0,0,0] for x in range(len(uniquestems))] #for 3d and 4d
	freqlist = [[0,0,0,0,0,0] for x in range(len(filestem))]	#for 2d classification

	i=0
	#inner = 6720		#for 4d
	#outer = 101		#for 4d
	#inner = 48			#for 3d
	#outer = 14140		#for 3d
	inner = 1			#for 2d
	outer = 14140*48	#for 2d
	
	for k in range(outer):
		category = int(matrix[k*inner][1])
		freqlist[k][5] = category
		for j in range(inner):
			freqlist[k][int(matrix[(k*inner)+j][0])]+=1
	return freqlist

def get_statistics(mylist):
	instances = [0,0,0,0,0]
	correct = [0,0,0,0,0]
	incorrect = [0,0,0,0,0]
	falsepositives = [0,0,0,0,0]
	confusionmatrix = [[0,0,0,0,0] for x in range(5)]

	for q in mylist:
		j = q[0:5]
		instances[q[5]]+=1	#another ad (or emci, lmci, etc.) subject in the dataset
		if j.index(max(j)) == q[5]:
			correct[q[5]]+=1
			confusionmatrix[q[5]][q[5]]+=1
		else:
			incorrect[q[5]]+=1
			falsepositives[j.index(max(j))]+=1
			confusionmatrix[q[5]][j.index(max(j))]+=1

	print(instances)
	print(correct)
	print(incorrect)
	print(falsepositives)
	print(confusionmatrix)
	print(sum(correct)/sum(instances))


fnamea = "weights00065results.csv"
fnameb = "classweightedresults.csv"

lista = freqlist(fnamea)
listb = freqlist(fnameb)
get_statistics(lista)
get_statistics(listb)

mod = 0
correct_per_slice = [0]*48
incorrect_per_slice = [0]*48

instances = [0,0,0,0,0]
correct = [0,0,0,0,0]
incorrect = [0,0,0,0,0]
falsepositives = [0,0,0,0,0]
confusionmatrix = [[0,0,0,0,0] for x in range(5)]

for i in range(len(lista)):
	mod = i%48
	first = lista[i][0:5]
	second = listb[i][0:5]
	# Error case
	if(lista[i][5]!=listb[i][5]):
		print("Something's messed up")
		print(lista[i][5], listb[i][5])
		quit()

	truth = lista[i][5]
	
	instances[truth]+=1	#another ad (or emci, lmci, etc.) subject in the dataset
	#emci case
	emci = 2
	smc = 4
	if(second.index(max(second))==emci):
		if(truth==emci):
			correct[truth]+=1
			confusionmatrix[truth][truth]+=1
			correct_per_slice[mod]+=1
		else:
			incorrect[truth]+=1
			falsepositives[emci]+=1
			confusionmatrix[truth][emci]+=1
			incorrect_per_slice[mod]+=1
	#smc case
	elif(second.index(max(second))==smc):
		if(truth==smc):
			correct[truth]+=1
			confusionmatrix[truth][truth]+=1
			correct_per_slice[mod]+=1
		else:
			incorrect[truth]+=1
			falsepositives[smc]+=1
			confusionmatrix[truth][smc]+=1
			incorrect_per_slice[mod]+=1
	else:	#not emci
		if first.index(max(first)) == truth:
			correct[truth]+=1
			confusionmatrix[truth][truth]+=1
			correct_per_slice[mod]+=1
		else:
			incorrect[truth]+=1
			falsepositives[first.index(max(first))]+=1
			confusionmatrix[truth][first.index(max(first))]+=1
			incorrect_per_slice[mod]+=1

print(instances)
print(correct)
print(sum(correct))
print(incorrect)
print(sum(incorrect))
print(falsepositives)
print(confusionmatrix)
print(sum(correct)/sum(instances))
print("Per Slice")
print(correct_per_slice)
print(sum(correct_per_slice))
print(incorrect_per_slice)
print(sum(incorrect_per_slice))
acc_per_slice = [0]*48
for j in range(len(correct_per_slice)):
	acc_per_slice[j] = correct_per_slice[j]/(incorrect_per_slice[j]+correct_per_slice[j])
	print("("+str(j)+","+str(acc_per_slice[j])+")")