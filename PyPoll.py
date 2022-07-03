#importing the csv file 
import os
import csv 
import sys

#Assign a variable to load a file from a path.
file_to_load = os.path.join('./Resources','election_results.csv')

#Assign a variable to save the file to a path.
#file_to_save = os.path.join('.','analysis','election_analysis.txt')
file_to_save = os.path.join('./analysis','election_analysis.txt')

# Increment each vote by 1
total_votes = 0 
#Candidate options and candidate votes
candintes_options = []
candidates_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
#with open(file_to_save,'w') as txt_file:

with open(file_to_load) as election_data:

    #TO Do: read and analyze data here.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
  #print(headers)

#Print each row in csv file
    for row in file_reader:
      #print(row)
      total_votes +=1
    
    #Print the candidates name from each row
      candidates_names = row[2]
    
     #If the candidate does not match any existing candidate add it the candidate list.
      if candidates_names not in candintes_options:
    
    # Add the candidate name to the cadidate list  
        candintes_options.append(candidates_names)
    
    #Begin tracking that candidate's vote count
        candidates_votes[candidates_names] = 0
    # Add a vote to that candidate's count
      candidates_votes[candidates_names] +=1


with open(file_to_save, "w") as txt_file:
   #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

      #Iterate through the candidate list
    for candidates_names in candidates_votes: 
            #Retrieve vote count of a candidate 
            votes = candidates_votes[candidates_names]
            #Calculate the percentage of votes 
            vote_percentage = float(votes) / float(total_votes) * 100
            #Print the candidate name and percentage of votes 

            candidate_results = (f"{candidates_names}: {vote_percentage:.1f}% ({votes:,})\n")
            
            #print each candidate's voter count and percentage to the terminal
            print(candidate_results)
            
            # Save the candidates results to our text file.
            txt_file.write(candidate_results)
              # Determine winning vote count and candidate
              # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                    # If true then set winning_count = votes and winning_percent =
                    # vote_percentage.
                    winning_count = votes
                    winning_percentage = vote_percentage
                    # And, set the winning_candidate equal to the candidate's name.
                    winning_candidate = candidates_names

            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")

            print(winning_candidate_summary)
              # Save the winning candidates results to the text file. 
            txt_file.write (winning_candidate_summary)  