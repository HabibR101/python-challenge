#%%

import os
import csv

#set variables

dates = []
total_rows = 0 
total = 0 
profit = []
ave_profit_change = []
greatest_increase = 0 
greatest_decrease = 0

#Path to open Budget Data

csvpath = os.path.join('/Users/HabibRehman/Documents/Data Analytics/Module_3/Starter_Code/Resources/budget_data.csv')


# Action to open CSV and read

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header as the first row

    csvheader = next(csvfile)
    print(f"Header: {csvheader}")

# Read and loop through the each row of data

    for row in csvreader:

        #total number of rows in data and add to a array
        total_rows += 1
        dates.append(row[0])

        #Calculate the total amount of profit and add to a array
        total += int(row[1])
        profit.append(int(row[1]))

# Loop and calculate changes between months. Checks for the average change and sets months or changes where conditions is satisfied

for i in range (len(profit)-1):
        avechange = profit[i+1] - profit[i]
        ave_profit_change.append(avechange)

        average_change = round(sum(ave_profit_change)/len(ave_profit_change),2)

        if(avechange>greatest_increase):
             greatest_increase_month = dates[i+1]
             greatest_increase = avechange

        if(avechange<greatest_decrease):
             greatest_decrease_month = dates[i+1]
             greatest_decrease = avechange


#Print results of analysis and then outputs text into txt file 

print("Financial Analysis")
print("-" * 25)
print(f"Total Months: {total_rows}") 
print(f"Total: $" + str(total))
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

output_path = os.path.join('/Users/HabibRehman/Documents/Data Analytics/Module_3/Starter_Code/PyBank/financial_analysis.txt')

with open(output_path, 'w', newline='') as txt:

    txt.write("Financial Analysis\n")
    txt.write("-" * 25)
    txt.write('\n')
    txt.write(f"Total Months: {total_rows}\n")
    txt.write('\n')
    txt.write(f"Total: ${total}\n")
    txt.write('\n')
    txt.write(f"Average Change: ${average_change}\n")
    txt.write('\n')
    txt.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt.write('\n')
    txt.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
 




# %%
