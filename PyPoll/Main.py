#%%

import os
import csv

#set variables to create stores variable and lists 

total_rows_votes = 0
candidate_list = []
voters_list = []

#Path to open election Data

csvpath = os.path.join('/Users/HabibRehman/Documents/Data Analytics/Module_3/Starter_Code/Resources/election_data.csv')


# Action to open CSV and read

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header as the first row

    csvheader = next(csvfile)
    print(f"Header: {csvheader}")
#code that loops across data set and then checks how many votes a candidate has. Then code then moves onto checking if name does not exist in the list. Adds the code to the list if not
#present and counts the amount of votes next to candidates. 
    for row in csvreader: 

        total_rows_votes += 1 

        if row[2] not in candidate_list:

            candidate_list.append(row[2])

            index = candidate_list.index(row[2]) 

            voters_list.append(1)  
        else:
            index = candidate_list.index(row[2])
            voters_list[index]+=1



# print results

print("Election Results")
print("-" * 25)
print(f"Total Votes:{total_rows_votes}")
print("-" * 25)
print(f"{candidate_list[0]}: {(voters_list[0]/total_rows_votes)*100:.3f}% ({voters_list[0]})")
print(f"{candidate_list[1]}: {(voters_list[1]/total_rows_votes)*100:.3f}% ({voters_list[1]})")
print(f"{candidate_list[2]}: {(voters_list[2]/total_rows_votes)*100:.3f}% ({voters_list[2]})")
print("-" * 25)
print(f"Winner: {candidate_list[voters_list.index(max(voters_list))]}")
print("-" * 25)

output_path = os.path.join('/Users/HabibRehman/Documents/Data Analytics/Module_3/Starter_Code/PyPoll/election_results.txt')


# export txt file of results

with open(output_path,'w',  newline='') as txt:
    txt.write("Election Results\n")
    txt.write('\n')
    txt.write("-" * 25)
    txt.write('\n')
    txt.write(f"Total Votes: {total_rows_votes}\n")
    txt.write('\n')
    txt.write("-" * 25)
    txt.write('\n')
    txt.write(f"{candidate_list[0]}: {(voters_list[0]/total_rows_votes)*100:.3f}% ({voters_list[0]})\n")
    txt.write('\n')
    txt.write(f"{candidate_list[1]}: {(voters_list[1]/total_rows_votes)*100:.3f}% ({voters_list[1]})\n")
    txt.write('\n')
    txt.write(f"{candidate_list[2]}: {(voters_list[2]/total_rows_votes)*100:.3f}% ({voters_list[2]})\n")
    txt.write('\n')
    txt.write("-" * 25)
    txt.write('\n')
    txt.write(f"Winner: {candidate_list[voters_list.index(max(voters_list))]}\n")
    txt.write("-" * 25)


# %%
