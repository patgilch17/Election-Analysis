import csv
import os

#assign a variable for the pash to the csv file.  Using os.path.join so that in case this is run on a different
#operating system the file path isn't messed up.  mac uses / windows uses \ resources/election_results.csv wouldn't run on windows.
filetoread = os.path.join('Resources','election_results.csv')

#assign a variable to the file we will write too
filetowrite = os.path.join('Analysis','election_analysis.txt')

#election_data = open(filetoread,'r')
#election_data.close()

# Initialize a total vote counter
total_votes = 0

# Initialize a list for my different candidates
list_candidates = []
#list_ballotIDs = []

candidate_votes = {}

#open election results and read the file
with open(filetoread,'r') as election_data:
    #To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    #print(headers)
    #print each row in the csv file
    for row in file_reader:
        #if row[0] not in list_ballotIDs:
        #    list_ballotIDs.append(row[0])

            total_votes += 1
            #checks if the candidate name has been used and adds it to a list if it has not
            candidate_name = row[2]
            if candidate_name not in list_candidates:
                list_candidates.append(candidate_name)

                #adds that name to the dictionary for candidate votes and sets that candidate equal to 0
                candidate_votes[candidate_name] = 0
            #increments the voting totals for that candidate
            candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(filetowrite,'w') as election_analysis:
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end="")
    election_analysis.write(election_results)
    
#print(total_votes)
#print(list_candidates)
#print(candidate_votes)
#winning = ""
#winning = list_candidates[0]
#indexplaceholder = 0
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    #determine the percentage of votes with a loop through the list of candidates
    for i in list_candidates:
        votes = candidate_votes[i]
        vote_percentage = (float(votes)/float(total_votes))*100
        candidate_results = (f"{i}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        election_analysis.write(candidate_results)
        #election_analysis.write(f"{i}: {vote_percentage:.1f}% ({votes:,})\n")
        #print(f"{i}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine who won
        #if winning != list_candidates[indexplaceholder] and candidate_votes[winning] < candidate_votes[i]:
        #    winning = i
        #indexplaceholder += 1
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = i
#print(f"{winning} won with {candidate_votes[winning]} votes")
    winning_candidate_summary = (
        f"---------------------------------\n"
    #f"{winning_candidate} won with {winning_percentage:.1f}% of the vote ({winning_count} total votes).\")
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------\n")
#print(winning_candidate_summary)
    print(winning_candidate_summary)
    election_analysis.write(winning_candidate_summary)
#print(len(list_candidates))

#open the text file to write in
#with open(filetowrite,'w') as election_analysis:

    #write to the text file
#    election_analysis.write("Counties in the Election \n")
#    election_analysis.write("----------------------\n")
#    election_analysis.write("Arapahoe\nDenver\nJefferson")
    #election_analysis.write("Denver, ")
    #election_analysis.write("Jefferson")
    #open(filetowrite,'w')




# Data needed via retrevial
#A) Total number of votes cast
#B) A complete list of candidates who received votes
#C) The percent of votes each candidate won
#D) The total numver of votes for each candidate
#E) The winner based on the popular vote

#close the 