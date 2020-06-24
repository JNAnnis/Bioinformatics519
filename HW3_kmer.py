#Homework 3 Problem 2


import sys


#Define input variables
DNAseq = sys.argv[1]
kLength = int(sys.argv[2])
cutoffN = int(sys.argv[3])


with open(DNAseq, 'r') as f:

	inSeq = f.readlines()

	LongString = ''
	for line in inSeq:
		LongString += line.strip() #create a string containing the DNA bases 
	
	totalLen = len(LongString)
	
	kDict ={} #initialize an empty dictionary
	for i in range(0, totalLen-kLength+1):
		kmer = LongString[i:i+kLength] #cut out each kmer
				
		if kmer in kDict:
			kDict[kmer] += 1 #if the kmer is already in the dictionary, add one to the value
		else:
			kDict[kmer] = 1	#if not, give it a value of one

	for kmer in kDict:
		if kDict[kmer] > cutoffN: #if the value for the kmer in the dictionary is greater than the cutoff number print it
			print(kmer + '\n')
	
