#Homework 9 Problem 2


import sys
from math import log


kLength = int(sys.argv[1]) #int makes the input an integer and not a string
inputFile = sys.argv[2]


def makePFM(sites, kLength): 
	
	pfm = {"A":[1]*kLength, "T":[1]*kLength, "C":[1]*kLength, "G":[1]*kLength}

	for kmer in sites: 
		for i in range(len(kmer)):
			letter = kmer[i] #pull out letter at ith position in kmer
			pfm[letter][i] += 1 #add one to the pfm value at that letter and position

	return  pfm


def makePPM(pfm, kLength):
	
	ppm = {}
	sumCounts1 = float(pfm["A"][0] + pfm["T"][0] + pfm["C"][0] + pfm["G"][0])
	
	for key in pfm:
		ppm[key] = [float(value/sumCounts1) for value in pfm[key]] #for each key in pfm, divide by the sum of the counts in 1st position
	
	return ppm
		

def scoreKmerPPM(kmer, ppm): 

	score = 1

	for i in range(len(kmer)):
		letter = kmer[i] #pull out the letter at ith position in kmer
		score *= ppm[letter][i] #the new score is the previous score multiplied by the value for the letter in the ith position of the kmer

	return score


def findBestKmer(sequence, ppm, kLength): #not sure if this is 100% correct

	bestProb = 0
	bestKmer = ""

	for i in range(0, len(sequence)-kLength+1):
		kmer = sequence[i:i+kLength] #get kmer
		prob = scoreKmerPPM(kmer, ppm) #get the probability for the kmer
		if prob > bestProb: #only if the probability of the kmer is greater than the current best probability, replace the best kmer and probabilty
			bestProb = prob
			bestKmer = kmer
				
	return bestKmer
	return bestProb


def infoContent(ppm, kLength):

	icTotal = 0
	
	for i in range(0, kLength): 
		posCount = 0 #contains the total count at that ith position
		
		for key in ppm:
			pValue = ppm[key][i] #get the values from the ppm
			posCount += pValue*log(pValue, 2) #update the posCount variable using the equation
		
		icTotal += posCount + 2 #add the posCount to the icTotal and then add 2

	return icTotal



kmers = []
with open(inputFile, 'r') as f:

	inSeq = f.readline() #get the first line only
	kmer0 = inSeq[0:0+kLength] #get the first kmer from the first line
	kmers.append(kmer0)


pfm0 = makePFM(kmers, kLength) #create the initial pfm and ppm 
ppm0 = makePPM(pfm0, kLength)


with open(inputFile, 'r') as f:

	inSeq = f.readlines()[1:] #pull out the other lines (excluding the first line)
		
	for line in inSeq: #each line is a new sequence
		seq = line.strip()
		bestKmer = findBestKmer(seq, ppm0, kLength) #get the best kmer from sequence and then add to the kmers list
		kmers.append(bestKmer)
		pfm0 = makePFM(kmers, kLength) #after getting the best kmer from the sequence, update the pfm and ppm
		ppm0 = makePPM(pfm0, kLength)


ppmIC = infoContent(ppm0, kLength) #get the IC for the completed kmers list


print "The kmers are:"
print '\n'.join(k for k in kmers)
print ""
print "The PPM is:"
print ('\n'.join("{}\t{}".format(k, v) for k, v in ppm0.items()))
print ""
print "The total information content is: " + str(ppmIC) 
