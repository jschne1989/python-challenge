import os
import csv
import sys

totalvotes = 0
candidateslist = []
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	#skip header
	next(csvreader, None)

#start for loop to run throw rows

	for row in csvreader:
		# Total number of votes (count rows)
		totalvotes = totalvotes + 1

		#List of candidates - unique values
		
		if row[2] not in candidateslist:
			candidateslist.append(row[2])


	print(str(totalvotes))
	print(candidateslist)
#Calculate percentage of votes for each candidate won

#calculate total number of votes for each candidate

#Find the winner - highest number of votes