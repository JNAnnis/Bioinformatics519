#Homework 5 Problem 1

import sys


#Define the input variables:
sequence1 = sys.argv[1]
sequence2 = sys.argv[2]


with open(sequence1, 'r') as s1, open(sequence2, 'r') as s2:  #open the sequence files
	
	seq1 = s1.readlines() #pull out the sequence from the file 
	seq2 = s2.readlines()
	
	if seq1[0][0] == '>': #if there is a header line
		seq1 = ''.join(i for i in seq1[1:len(seq1)]) #join all of the seqence lines, ignore the header
	else:
		seq1 = ''.join(i for i in seq1) #if there isn't a header, just join all of the lines
		
	if seq2[0][0] == '>':
		seq2 = ''.join(j for j in seq2[1:len(seq2)])
	else:
		seq2 = ''.join(j for j in seq2)

	#Print the sequences
	print "Seq. 1 is", seq1
	print "Seq. 2 is", seq2

	for k in range(0, len(seq1)): #loop through the bases in seq1
		for l in range(0, len(seq2)): #loop through the bases in seq2; loops through all the seq2 bases for each seq1 base
			if seq1[k] == seq2[l]: # if the bases are the same 
				print '*',
			else:
				print ' ',
		
		print '\n' #print a new line
