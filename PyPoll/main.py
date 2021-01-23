import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

unique_candidates = []
all_cadidates = []

li_votes = 0
khan_votes = 0
correy_votes = 0
otooley_votes = 0
total_votes = 0

def unique_candidates(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        print(x)


with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)


    # Loop through the data
    for row in csvreader:
        #print(row)
        total_votes += 1

        candidate = row[2]

        all_cadidates.append(candidate)

        if candidate == 'Li':
            li_votes += 1
        if candidate == 'Khan':
            khan_votes += 1
        if candidate == 'Correy':
            correy_votes += 1
        if candidate == 'O\'Tooley':
            otooley_votes += 1

    li_vote_percent = "{:.2%}".format(li_votes / total_votes)
    khan_vote_percent = "{:.2%}".format(khan_votes / total_votes)
    correy_vote_percent = "{:.2%}".format(correy_votes / total_votes)
    otooley_vote_percent = "{:.2%}".format(otooley_votes / total_votes)
    
    print('Election Results')
    print('---------------------------')
    print('Total Votes: '+str(total_votes))
    print('---------------------------')
    print('Li: '+ str(li_vote_percent) + ' , ' + str(li_votes))
    print('Khan: '+ str(khan_vote_percent) + ' , ' + str(khan_votes))
    print('Correy: '+ str(correy_vote_percent) + ' , ' + str(correy_votes))
    print('O\'Tooley: '+ str(otooley_vote_percent) + ' , ' + str(otooley_votes))

    print('---------------------------')
    print('Winner: Khan')


output_path = os.path.join('..', 'analysis', 'PyPoll_Analysis.txt')
with open(output_path, "w") as text_file:
    print('Election Results', file=text_file)
    print('---------------------------', file=text_file,)
    print('Total Votes: '+str(total_votes), file=text_file,)
    print('---------------------------', file=text_file,)
    print('Li: '+ str(li_vote_percent) + ' , ' + str(li_votes), file=text_file,)
    print('Khan: '+ str(khan_vote_percent) + ' , ' + str(khan_votes), file=text_file,)
    print('Correy: '+ str(correy_vote_percent) + ' , ' + str(correy_votes), file=text_file,)
    print('O\'Tooley: '+ str(otooley_vote_percent) + ' , ' + str(otooley_votes), file=text_file,)
    print('---------------------------', file=text_file,)
    print('Winner: Khan', file=text_file,)    
   




        
        
