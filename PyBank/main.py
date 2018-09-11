import os
import csv
import sys

#month count variable
month_count = 0

#total sum variable
totalrev = 0

#list to keep track of differences
avg = []

#store previous row value
prevrow = 0
#store difference
dif = 0

#average of list of differences

difavg = 0

#lowest value

low = 0
lowlist = []

#highest value

hi = 0
hilist = []
#define csv path to file
csvpath = os.path.join('Resources', 'budget_data.csv')
finalpath = os.path.join('Resources', 'final_budget_data.txt')

#open CSV file to read
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	#skip header
	next(csvreader, None)

#create for loop to run through rows

	for row in csvreader:
		#Count number of months
		month_count = month_count + 1
		#sum profit/losses
		totalrev = int(row[1]) + totalrev

	#create new list t+o pull difference between rows and store value
	#take average of list
		dif = int(row[1]) - prevrow

		avg.append(dif) 
		#reset prevrow value for next iteration
		prevrow = int(row[1])
		#take average of list
		#create value to store lowest number
		if int(row[1]) < int(low):
			low = row[1]
			lowlist = [row[0], "$" + str(row[1])]

		#create value to store highest number
		if int(row[1]) > int(hi):
			hi = row[1]
			hilist = [row[0], "$" + str(row[1])]

	del avg[0]
	difavg = sum(avg)/len(avg)





	print("Financial Analysis")
	print("______________________")
	print("Total Months: " + str(month_count))
	print("Total: " + "$" + "{0:.2f}".format(totalrev))
	print("Average Change: " + "$" + "{0:.2f}".format(difavg))
	print("Greatest Increase in Profits: " + str(hilist))
	print("Greatest Decrease in Profits: " + str(lowlist))

def out_data():
	return ("Financial Analysis \n"
	 + "______________________ \n" +
	"Total Months: " + str(month_count) + "\n" +
	"Total: " + "$" + "{0:.2f}".format(totalrev) + " \n" +
	"Average Change: " + "$" + "{0:.2f}".format(difavg) + " \n" + 
	"Greatest Increase in Profits: " + str(hilist) + " \n"
	"Greatest Decrease in Profits: " + str(lowlist))

output = out_data()
file = open(finalpath,"w")
file.write(str(output))
file.close()

# end for loop

#print values
#print to file