#PyBank

#import csv file
import os
import csv
csvpath = os.path.join("PyBank.csv")

suma = 0
count = 0
ave = 0
increase = 0
deacrease = 0

with open (csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    


#Print dataset to corroborate successful upload
    for row in csvreader:
        date = row[0]
        prf_loss = (row[1])

#Count the total number of months in dataset
        count = sum(1 for row in csvfile)

#Count the net total amount of "Profit/Losses" over the entire period
        suma += float(prf_loss)

#Calculate the average of the changes in "Profit/Losses" over the entire period
        ave = suma / count

#The greatest increase in profits (date and amount) over the entire period
        for row in range(count):
        
            increase = max(prf_loss)

#The greatest decrease in profits (date and amount) over the entire period
            decrease = min(prf_loss)

#Print the results
        print("Financial Analysis")
        print("-------------------------------")
        print("Total Months: " + str(count))
        print("Total: $" + str(suma))
        print("Average Change: $" + str(ave))
        print("Greatest increase in profits: " + str(increase))
        print("Greatest decrease in profits: " + str(decrease))

#import to CSV

myData = ["Financial Analysis","Total Months: " + str(count),"Total: $" + str(suma),"Average Change: $" + str(ave),"Greatest increase in profits: " + str(increase),"Greatest decrease in profits: " + str(decrease)]
myFile = open("Analysis","results.csv","w")

with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)




    

    

        
        