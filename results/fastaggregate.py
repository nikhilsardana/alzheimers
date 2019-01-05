#Nikhil Sardana
#11/8/17
# O(n) time
# **********************************
# Commented lines for 3D Aggregation
# **********************************
filename = "classweightedresults.csv"
with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content] 

matrix = [x.split(',') for x in content]

#filestem = [x[2].split('-')[0] for x in matrix]
filestem = [x[2].split('slice_')[0] for x in matrix]

uniquestems = set(filestem)
freqlist = [[0,0,0,0,0,0] for x in range(len(uniquestems))]

i=0
inner = 6720
outer = 101
#inner = 48
#outer = 14140

for k in range(outer):
	category = int(matrix[k*inner][1])
	freqlist[k][5] = category
	for j in range(inner):
		freqlist[k][int(matrix[(k*inner)+j][0])]+=1
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
