# set dependencies
import csv
import os
#copy the path to the csv file
variable = os.path.join("Resources", "budget_data.csv")
#open the csv file
with open(variable,"r") as csvfile:
    #read the csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    csv_header = next(csvreader)
    #set variables
    total_months = 0
    total = 0
    average_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    #set lists
    month = []
    profit_loss = []
    change = []
    #loop through the csv file
    for row in csvreader:
        #add to total months
        total_months += 1
        #add to total
        total += int(row[1])
        #add to month list
        month.append(row[0])
        #add to profit_loss list
        profit_loss.append(int(row[1]))
    #loop through the profit_loss list
    for i in range(len(profit_loss)-1):
        #add the difference between the current and next month to the change list
        change.append(profit_loss[i+1]-profit_loss[i])
        #find the average change
        average_change = sum(change)/len(change)
        #find the greatest increase
        greatest_increase = max(change)
        #find the greatest decrease
        greatest_decrease = min(change)
    #find the index of the greatest increase
    greatest_increase_index = change.index(greatest_increase)
    #find the index of the greatest decrease
    greatest_decrease_index = change.index(greatest_decrease)
    #find the month of the greatest increase
    greatest_increase_month = month[greatest_increase_index+1]
    #find the month of the greatest decrease
    greatest_decrease_month = month[greatest_decrease_index+1]
    #print the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
