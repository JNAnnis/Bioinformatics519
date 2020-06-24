#Homework 2 Problem 2


#Define the two sequences as strings:
seq1 = 'ATGTCAGATCGG'
seq2 = 'TCGATCGATTGTTTAACTGAGGGGGCT'

#Create a function that slices out the first and last codons from the sequence:
def FirstandLast(seq):
	print "For the sequence:", seq
	print "The first codon is:", seq[:3] #gets the first codon and prints it
	print "The last codon is:",  seq[-3:] #gets the last codon and prints it
	print " "

#Call the function on both sequences:
FirstandLast(seq1)
FirstandLast(seq2)

