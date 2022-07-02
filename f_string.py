my_votes = int(input('How many votes did you get in the election?'))
total_votes = int(input("What were the total votes in the election? "))
print (f'I recieved  {my_votes/total_votes * 100}  % of the total votes')

message_to_candidate = (
    f' you recieved {my_votes: ,} votes'
    f' there were {total_votes: ,} total votes'
    f' you recieved {my_votes/total_votes * 100:.2f} % percentage of the votes'
)
print (message_to_candidate)