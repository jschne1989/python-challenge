import os
import csv
import sys

totalvotes = 0
candidateslist = []
candidatevotes = []
percent = 0
candidate_percent = []
current_candidate = 0



csvpath = os.path.join('Resources', 'election_data.csv')
finalpath = os.path.join('Resources', 'final_poll_data.txt')

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	#skip header
	next(csvreader, None)

#start for loop to run through rows

	for row in csvreader:
		# Total number of votes (count rows)
		totalvotes = totalvotes + 1
		current_candidate = row[2]

		#List of candidates - unique values
		if current_candidate in candidateslist:
			candidate_index = candidateslist.index(current_candidate)
			candidatevotes[candidate_index] += 1

		#otherwise, add this candidate to the list and give them 1 vote
		else: 
			candidateslist.append(current_candidate)
			candidatevotes.append(1)

	for candidate in candidatevotes:
		percent = (candidate)/totalvotes
		percent_format = "{0:.0%}".format(percent)
		candidate_percent.append(percent_format)

	winner_index = candidatevotes.index(max(candidatevotes))
	winner = candidateslist[winner_index]

	final_candidate_list = list(zip(candidateslist, candidatevotes, candidate_percent))
#Calculate percentage of votes for each candidate won

#calculate total number of votes for each candidate

#Find the winner - highest number of votes


	# print(str(totalvotes))
	# print(candidateslist)
	# print(candidatevotes)
	# print(candidate_percent)
	# print(winner)


print("Election Results")
print("_ _ _ _ _ _ _ _ _ _ _ _ ")
print(" ")
print("Total Votes: " + str(totalvotes))
print("_ _ _ _ _ _ _ _ _ _ _ _ ")
#print('\n'.join('{}' for _ in range(len(final_candidate_list))).format(*final_candidate_list))
for each in final_candidate_list:
	print(each, sep='\n')
print("_ _ _ _ _ _ _ _ _ _ _ _ ")
print(" ")
print("Winner: " + str(winner))
print("_ _ _ _ _ _ _ _ _ _ _ _ ")

def out_data():
	return ("Election Results \n"
		+ "- - - - - - - - - - - \n" +
		"Total Votes: " + str(totalvotes) + "\n" +
		"- - - - - - - - - - - \n" +
		('\n'.join('{}' for _ in range(len(final_candidate_list))).format(*final_candidate_list)) + "\n" +
		" - - - - - - - - - - \n" + 
		"Winner: " + str(winner) + "\n" + 
		" - - - - - - - - - - \n")


output = out_data()
file = open(finalpath,"w")
file.write(str(output))
file.close()