#Homework 6 Problem 5


import sys


#Define input variables
inputFile = sys.argv[1]


with open(inputFile, 'r') as f:
	
	inLines = f.readlines()

	inTable = []
	for line in inLines:
		if line[0] != '#':
			inTable.append(line.strip().split('\t'))
	
	countHits = 0 #counter to count the number of hits
	countAL = 0 #counter to count the alignment lengths less than 20
	
	reducedList = []
	for row in inTable:
		queryID = row[0] #get only the relevent columns
		subjectID = row[1]
		pIdentity = float(row[2]) #convert the values to floating pts
		alignLen = float(row[3])
		eValue = float(row[10])
		
		if queryID != subjectID and pIdentity >= 95.0 and eValue < 0.1: #only add the 5 fields if the meet this criteria
			reducedList.append([queryID, subjectID, pIdentity, alignLen, eValue])
			countHits += 1 #if the row is added, count it as a hit
		
			if alignLen < 20.0: 
				countAL += 1 #count if the alignment length if less than 20
		
	 
with open('ex5.output', 'w') as outf:
	print >> outf, "Fields: Query ID, Subject ID, % Identity, Alignment Length, E-value"
	for line in reducedList:
		print >> outf, line

with open('ex5.stats', 'w') as outs:
	print >> outs, "The total number of hits is", countHits
	print >> outs, "The number of hits with alignment length less than 20 is", countAL
