# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# print(file_to_load)
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# Intialize a county name list and county votes dictionary
county_names = []
county_votes = {}
                    
# Track the winning candidate vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county turnout with a string and set the largest county vote count to 0, as an integer
largest_county_turnout = ""
largest_county_vote = 0

#read the csv and convert it to a list of dictionaries referencing the initial file we loaded in as the data
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
    
    # For loop to run all rows in the CSV file
    for row in reader:
        # Add to the total vote count.
        total_votes = total_votes + 1
        # Get the candidate name from each row from the CSV file, reminder: index starts at 0, 2 really means row 3 in normal human talk
        candidate_name = row[2]
        # Get the county name from each row, which in the file, it is row 2
        county_name = row[1]

        # If the candidate does not match any existing candidate
        # add it to the list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list, append function adds new value to data list
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count. finds votes registered or corresponding to candidate name values
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that a county is not found in the list, if this is the case
        #use the append function to create a new value for the mismatch
        if county_name not in county_names:
            # Add it to the list of county, append function
            county_names.append(county_name)

            # Begin tracking the county votes corresponding to the candidate value in the CSV file
            county_votes[county_name] = 0
        #when a line corresponds with a vote to a candidate, start the counter to tally up all votes
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal (separate from writing to a txt_file, this command needs to be remembered)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n"
    )
    print(election_results, end="")    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    # establish a for loop to stem from the county dictionary
    for county in county_votes:
        # retrieve the votes corresponding to each county
        county_vote = county_votes[county]
        #calculate the percentage of votes per county out of the total votes collected
        county_percent = int(county_vote)/int(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
        )
        #print the county results to the terminal
        print(county_results, end="")
        #using the output text file, save the same results to this election_analysis.txt
        txt_file.write(county_results)

        # Write an if statement to to determine the largest voting county and output the total count
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

    # Print the largest county turnout to the terminal
    largest_county_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout is in ({largest_county_turnout}!!!)\n"
        f"-------------------------\n"
    )
    print(largest_county_turnout)
    
    #Save the same terminal information to the election_analysis.txt
    txt_file.write(largest_county_turnout)

    # Save the final candidate results to the text file.
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = int(votes)/int(total_votes) * 100
        candidate_results = (
            f"{candidate}: (received {vote_percentage:.1f}%) of the votes, which was a total of ({votes:,}) votes\n"
        )

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner aka the supastar: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage (THE GOAT): {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        )
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
