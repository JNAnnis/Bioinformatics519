#Homework 5 Problem 2

import sys


#Define the input variables:
sequence1 = sys.argv[1]
sequence2 = sys.argv[2]
window = int(sys.argv[3])
cutoff = int(sys.argv[4])

with open(sequence1, 'r') as s1, open(sequence2, 'r') as s2:  #open the sequence files
	
	seq1 = s1.readlines() #pull out the sequence from the file 
	seq2 = s2.readlines()
	
	if seq1[0][0] == '>': #get rid of the header if there is one (same as problem 1)
		seq1 = ''.join(i for i in seq1[1:len(seq1)])
	else:
		seq1 = ''.join(i for i in seq1)
		
	if seq2[0][0] == '>':
		seq2 = ''.join(j for j in seq2[1:len(seq2)])
	else:
		seq2 = ''.join(j for j in seq2)

	#Print the sequences
	print "Seq. 1 is", seq1
	print "Seq. 2 is", seq2

	for k in range(0,len(seq1)-window+1): #loop through seq1 then seq2, taking into account the window size
		for l in range(0,len(seq2)-window+1):
			counter = 0 #initialize a counter to count the number of matches
			for m in range(k,k+window): #m and n loops create the actual window size/shape
				for n in range(l,l+window):		 
					if m-k == n-l: #gives you the diagonal
						if seq1[m]==seq2[n]: #if the bases are the same, add 1 to the counter
							counter += 1

			if counter > cutoff: #if there are more matches than some cutoff number, print a * on the diagonal
				print '*',
			else:
				print ' ',
		
		print '\n' #print new line
