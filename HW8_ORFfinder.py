#Homework 8 Problem 1


import sys
from codondictionary import codon_dictionary


inputFile = sys.argv[1]


with open(inputFile, 'r') as f:

	inputSeq = f.readlines()[1:] #skip the header line

	sequence = ''
	for line in inputSeq:
		sequence += line.strip() #compile the bases into a string

	seqEnd = len(sequence) #get the sequence length


	for i in range(3): #determine the reading frame
		aaSequence = '' #initialize amino acid sequence string

		for j in range(i, seqEnd, 3): #loop through the sequence for each frame
			codon = sequence[j:j+3] #pull out the codon from the sequence
			
			if len(codon) == 3: #make sure the codon has 3 bases
				aminoAcid = codon_dictionary[codon] #lookup the codon in the dictionary
				aaSequence += aminoAcid #add the amino acid to the string	
		
			aaList  = aaSequence.split('_')	#split the amino acid sequence string by the stop codon
				
		for proteinSeq in aaList:  #for each sequence in the list, if the lenght is greater than or equal to 30, print it
			if len(proteinSeq) >= 30:
				print 'frame ' + str(i+1) + ' :' + ' ' + str(len(proteinSeq)) + ' ' +  proteinSeq			
