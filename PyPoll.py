#the data we need to retrieve
#1. total number of votes cast
#2. complete list of candidates who received votes
#3. percentage of votes each candidate received
#4. total number of votes each candidate won
#5. winner of election based on popular vote

import csv
import os 

file_to_load = os.path.join("/Users/michaeldemarco/Documents/GW/PyPoll/Resources/election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []

#declare empty vote dictionary for each candidate
candidate_votes = {}

#set the winning vote count and percentage to 0, per usual
#winning_candidate is a string so initiate it as one
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#open the election results and read the file
election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
#read/print header row
    headers = next(file_reader)
       
       #if we wanted to print headers
       #print(headers)

#print each row in the csv file
    for row in file_reader:
        
        #if we want to print all rows
        #print(row)

        #add to the vote count, the += just shorthand to do total_votes = total_votes + 1
        total_votes += 1

        #print candidate name from each row
        candidate_name = row[2]

        #add the candidate name to the candidate list, 
        #if candidate does not match existing candidate add it
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #track candidate vote counts
            candidate_votes[candidate_name] = 0
       
        #add a vote to the count of each candidate, has to be outside the if loop
        candidate_votes[candidate_name] += 1
        
#save the results to our text file
with open(file_to_save, "w") as txt_file:
   
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print(election_results, end="")
    
    #save the final vote count to a text file
    txt_file.write(election_results)

    #iterate through the candidate list
    for candidate_name in candidate_votes:
    
    #retrieve vote count per candidate
        votes = candidate_votes[candidate_name]
        
        #percentage calc
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #add each candidates results to the election_analysis.txt file
        #place the former print statement data into a new variable
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        #similar to the other print commands in this file, we print out the candidate results
        print(candidate_results)

        #write directly to the file that was called out in the file to save command earlier
        txt_file.write(candidate_results)
        
        #the if loop to print out general summary data
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
        
        #first prints the total results to include the candidate name, vote percentage to 1 decimal point, and total
            #print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n") --> this was moved upwards

    #now that the general voting data is printed
    #identify the summary highlighting the winner with winning_candidate_summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"-------------------------\n"
        )
    print(winning_candidate_summary)

    #save the winning candidate results to the same txt file
    txt_file.write(winning_candidate_summary)

    #print out the voter dictionary
    #print(candidate_votes)

    #print candidate list
    #print(candidate_options)

    #print total votes
    #print(total_votes)

    #to do: perform analysis

    #print(election_data)


    #close the file
    election_data.close()


    open(file_to_save, "w")


    #print out text to new election_analysis.txt 
    #outfile = open(file_to_save, "w")
    #outfile.write("Hello World")
    #outfile.close()

    #2nd way to write to a txt file using the write() command
    #with open(file_to_save, "w") as txt_file:
    #txt_file.write("Arapahoe\nDenver\nJefferson")
        
        