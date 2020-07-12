#PyPoll

#import csv file
import os
import csv
csvpath = os.path.join("PyPoll.csv")

cand = ["Khan","Correy","Li","O'Tooley"]
khanList = []
correyList = []
liList = []
tooList = []
kvote = 0



with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
  

    for row in csvfile:

                
#Count the total number of votes cast
        count = sum(1 for row in csvfile)

#A complete list of candidates who received votes
        if row[2] == "Khan":
                kvote = kvote =+ 1
        elif row[2] == "Correy":
                correyList.append(count + 1)
        elif row[2] == "Li":
                liList.append(count + 1)
        elif row[2] == "O'Tooley":
                tooList.append(count + 1)        

                


#Print the results
    print("Election Results")
    print("-------------------------------")
    print("Total Votes: " + str(count))
    print("Candidates: 1) " + cand[0] + " 2) " + cand[1] + " 3) " + cand[2] + " 4) " + cand[3])
    

#import to csv

myData = ["Total votes: ", str(count),"Candidates: 1) " + cand[0] + " 2) " + cand[1] + " 3) " + cand[2] + " 4) " + cand[3]]
myFile = open("resultsPyPoll.csv","w")

with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)