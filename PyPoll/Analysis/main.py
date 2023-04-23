import os
import csv
#set path for file
csvpath = os.path.join("Resources", "election_data.csv")
#open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    next(csvreader)
    #create empty lists
    candidates = []
    votes = []
    #loop through rows
    for row in csvreader:
        #add candidates to list
        candidates.append(row[2])
    #create dictionary
    candidate_votes = {}
    #loop through candidates
    for candidate in candidates:
        #if candidate is in dictionary, add 1 to their vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        #if candidate is not in dictionary, add them and set their vote count to 1
        else:
            candidate_votes[candidate] = 1
    #print results
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(len(candidates)))
    print("-------------------------")
    #loop through dictionary
    for key, value in candidate_votes.items():
        #print candidate name and percentage of votes
        print(key + ": " + str(round((value/len(candidates))*100, 3)) + "% (" + str(value) + ")")
    print("-------------------------")
    #find winner
    winner = max(candidate_votes, key=candidate_votes.get)
    print("Winner: " + winner)
    print("-------------------------")
