#Homework 3 Problem 1


from pprint import pprint
from decimal import *


seqList = []
with open('read1.txt', 'r') as a, open('read2.txt', 'r') as b: #open each file and combine the datta into one array called seqList
	for line in a:
		line = line.strip().split('\t') 
		Seq = line[0]
		count = int(line[1]) #make the count string  an integer
		seqList.append([Seq, count]) #create an array of arrays
	
	for line in b:
		line = line.strip().split('\t')
		Seq = line[0]
		count = int(line[1])
		seqList.append([Seq, count])



with open('targets.tsv','r') as c: #open the target table, format it, then assign it to a variable
	c_read = c.readlines()
	c_table = []
	for line in c_read:
		c_table.append(line.strip().split('\t'))


countList = []
for arrays in c_table:
	counter = 0 #initialize the counter that keeps track of the counts for each read
	for tags in seqList:
		if arrays[5] in tags[0]:
			counter += tags[1]
	countList.append(counter) #add the final count to an array		

			
totalcounts = sum(countList) #get the total number of counts
normcounts = [x/float(totalcounts) for x in countList] #calculate the normalized counts
normcounts = [float(Decimal("%.6f" % k)) for k in normcounts] #truncates the number of decimal places


with open('targets.tsv','r') as d:
	d_read = d.readlines()
	d_table = []
	for line in d_read:
		d_table.append(line.strip().split('\t'))
	for i,x in enumerate(countList): #add the counts to the table
		d_table[i].insert(6, x)
	for j,y in enumerate(normcounts): #add the normalized counts to the table
		d_table[j].insert(7, y)
	#Output = sorted(d_table, key=lambda l:l[6], reverse = True)  #sort the table

pprint(d_table)


