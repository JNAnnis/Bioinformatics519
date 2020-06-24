#Homework 2 Problem 4


from  random import choice

base = ['A', 'T', 'C', 'G'] #define the bases as an array

i = 0 #initialize while loop counter

while i < 5: #generate 5 sequences

	seqString = '' #initialize the string where the chosen bases will be stored

	for j in range(10): #this loop uses choice to randomly choose 10 bases	
		seqString += choice(base) #add the chosen base to the string

	print 'Random sequence', i, ':', seqString #print the string
	
	i += 1 #increase the counter
