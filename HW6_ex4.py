#Homework 6 Problem 4


import sys

#define input variables
inputFile = sys.argv[1]


with open(inputFile, 'r') as f:
	
	inLines = f.readlines()
	
	inTable = []
	for line in inLines:
		if line[0] != '#':
			inTable.append(line.strip().split('\t'))

	
	myQueries = [row[0] for row in inTable] #pull out only the query ID
	qSet = set(myQueries) #use set to get a list of only unique values
	numQueries = float(len(qSet)) #count the number of queries

	myHits = [row[0] + row[1] for row in inTable] #pull out both the query and subject id and concatenate them
	hSet = set(myHits) #get only the unique values from the list
	numHits = float(len(hSet)) #count the number of hits

	avgHpQ = numHits/numQueries #calculate the average hits per query

	print "The total hits is", numHits
	print "The total queries is", numQueries
	print "The average hits/query is", avgHpQ
