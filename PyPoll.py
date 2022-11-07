import csv
import os

#assign a variable for the pash to the csv file.  Using os.path.join so that in case this is run on a different
#operating system the file path isn't messed up.  mac uses / windows uses \ resources/election_results.csv wouldn't run on windows.
filetoread = os.path.join('Resources','election_results.csv')

#assign a variable to the file we will write too
filetowrite = os.path.join('Analysis','election_analysis.txt')

#election_data = open(filetoread,'r')

#election_data.close()

#open election results and read the file
with open(filetoread,'r') as election_data:
    #To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    print(headers)
    #print each row in the csv file
    for row in file_reader:
        print(row)


#open the text file to write in
with open(filetowrite,'w') as election_analysis:

    #write to the text file
    election_analysis.write("Counties in the Election \n")
    election_analysis.write("----------------------\n")
    election_analysis.write("Arapahoe\nDenver\nJefferson")
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