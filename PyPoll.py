# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candiates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Resources/election_results.csv

#Import the datetime class from the datetime module.
#import datetime as dt
#importing the csv file 
import os
import csv 
import sys

#Assign a variable to load a file from a path.
#file_to_load = ('./Resources/election_results.csv')

#election_data = open(file_to_load,'r')
#print(election_data)

# To do: perform analysis

#Close the file. 
#election_data.close()
#file_to_load = os.path.join('.','Resources','election_results.csv')

#Assign a variable to load a file from a path.
file_to_load = os.path.join('./Resources','election_results.csv')

#file_to_load = os.path.join(os.path.sep,'Users','dominiqueherring','Desktop','Analysis Projects','Election_Analysis-','Resources','election_results.csv')

#Assign a variable to save the file to a path.
#file_to_save = os.path.join('.','analysis','election_analysis.txt')
file_to_save = os.path.join('./analysis','election_analysis.txt')



#Open the election results and read the file.
#with open(file_to_save,'w') as txt_file:

with open(file_to_load) as election_data:

    #TO Do: read and analyze data here.
  file_reader = csv.reader(election_data)

# Print the header row.
  headers = next(file_reader)
  print(headers)


     #for row in file_reader:
      # print(row)

#Read the file object with the reader function.
  #file_reader = csv.reader(election_data)

#Print each row in the CSV file.


#Create a filename to variable to a direct or or indirect path to the file. 

#file_to_save = os.path.join(

# Use the open statement to open the file as a text file. 

#outfile = open(file_to_save, 'w')

#write some data to the file
  
  #txt_file.write('Counties in the Election\n')
  #txt_file.write('--------------\n')
  #txt_file.write('Arapahoe\nDenver\nJefferson')
  
  #txt_file.write('Denver, ')
  #txt_file.write('Jefferson, ')

#close the file
#outfile.close()

#Open the election results and read the file.
#with open(file_to_load) as election_data:
#election_data = open(file_to_load, 'r')

#To do: perform analysis. 
  # print (election_data)

#Close the file
#election_data.close()

# Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
#Print the present time
# print ('The time right now is', now#
#