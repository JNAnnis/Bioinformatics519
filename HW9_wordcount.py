#Homework 9 Problem 1


import sys
import string


kLength = int(sys.argv[1]) #variable for the length of the k-mer
inputFile = sys.argv[2]


with open(inputFile, 'r') as f:
	
	inputSeqs = f.readlines() #get all the sequences
	
	seqList = []
	for seq in inputSeqs:
		seqList.append(seq) #add the forward sequence to the list
		rcSeq = seq[::-1].translate(string.maketrans("ATCG", "TAGC")) #make the reverse complement and then add to the list
		seqList.append(rcSeq)

	
	kmerDict = {}
	for seq in seqList:
		for i in range(0, len(seq)-kLength+1):
			kmer = seq[i:i+kLength] #pull out the kmer
			kmerDict[kmer] = kmerDict.get(kmer, 0)+1 #add it to the dictionary or update the count


	bestKmerList = []
	bestKmerCount = 0
	kmerList = list(kmerDict.keys()) #get all the keys
	for key in kmerDict:
		count = kmerDict[key] #get the count for the key in dictionary
		if count > bestKmerCount: #if the count is greater than the current best count, replace both the best count and best kmer
			bestKmerCount = count
			bestKmerList = [key]
		if count == bestKmerCount: #if the count equals the current best count, add it to the kmer list
			bestKmerList.append(key)

	
	finalKmerList = set(bestKmerList) #my kmer list had a repeated key, so to get a list of distinct kmers, I called set() on the list

	print 'Max Count: ' + str(bestKmerCount)
	print 'Max ' + str(kLength) + '-mers: ' + ", ".join(i for i in finalKmerList)
	
