#Homework 2 Problem 5


from string import *  

#Define the function that produces the reverse complement:
def reverse_comp(seq): 
	seqUp = upper(seq) #make all letters uppercase

	OldBase = 'ATGC' #The bases in the input sequence
	NewBase = 'TACG' #The new bases the old bases become in the complement sequence

	BaseChange = maketrans(OldBase, NewBase) #make the table that translate function will use 

	seqComp = translate(seqUp, BaseChange) #convert the old bases to the new bases

	seqRevComp = seqComp[::-1] #reverse the complement sequence through slicing
	
	print seqRevComp #prints out the sequence

	return seqRevComp #returns the sequence so that it can be used...
			#...as an argument to test the function with assertions


#Call the function on some sequences
#If the assertion is true, when the program is run, there should be no Assertion Error
assert reverse_comp('AtcGATCG') == 'CGATCGAT'
assert reverse_comp('ataaccggact') == 'AGTCCGGTTAT'
assert reverse_comp('CTGCTGCCCAAAAC') == 'GTTTTGGGCAGCAG'
