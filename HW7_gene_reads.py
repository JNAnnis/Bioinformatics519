#Homework 7


header = ['Gene Name', 'HBR 1', 'HBR 2', 'HBR 3', 'UHR 1', 'UHR 2', 'UHR 3']

countList = [] #this will be the table containing all the counts of each gene

with open('HBR1align.bed', 'r') as f, open('HBR2align.bed', 'r') as g, open('HBR3align.bed', 'r') as h, open('UHR1align.bed', 'r') as j, open('UHR2align.bed', 'r') as k, open('UHR3align.bed', 'r') as l:
	for line in f:
		line = line.strip().split('\t')
		geneName = line[3] #extract the names of the genes
		count1 = line[5] #extract the counts of the gene
		countList.append([geneName, count1]) #creates a list of sublists

	#This process repeats for the remaining 5 files
	newList =[] #define an empty list to hold the counts
	for line in g:
		line = line.strip().split('\t')
		count2 = line[5] #extract the counts
		newList.append(count2) #add each count to the list
	for i in range(len(countList)):
		countList[i] += [newList[i]] #add the new counts to the ends of each sublist

	newList2 = []
	for line in h:
		line = line.strip().split('\t')
		count3 = line[5]
		newList2.append(count3)
	for i in range(len(countList)):
		countList[i] += [newList2[i]]
	
	newList3 = []
	for line in j:
		line = line.strip().split('\t')
		count4 = line[5]
		newList3.append(count4)
	for i in range(len(countList)):
		countList[i] += [newList3[i]]
	
	newList4 = []
	for line in k:
		line = line.strip().split('\t')
		count5 = line[5]
		newList4.append(count5)
	for i in range(len(countList)):
		countList[i] += [newList4[i]]

	newList5 = []
	for line in l:
		line = line.strip().split('\t')
		count6 = line[5]
		newList5.append(count6)
	for i in range(len(countList)):
		countList[i] += [newList5[i]]
	
countList.insert(0, header) #add the header to the beginning of the list of sublists


with open('HW7_gene_file.csv', 'w') as outf:
	outf.writelines('\t'.join(i) + '\n' for i in countList) #write out the list of sublists to a tab delimited file
