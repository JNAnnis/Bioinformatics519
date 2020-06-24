#Homework 2 Problem 3


seq = 'CGTAGATTCCTA' #define the sequence as a string

seqU = seq.replace('T', 'U') #use replace to change T to U

for i in range(len(seqU)): #use len to get sequence length; loop through each base in the sequence
	print seqU[i] #index to only print one base on each line

