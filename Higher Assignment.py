#Stephen Wallace 6W
#Choral Shields Higher assignment
import csv
#Import the csv library
import datetime
#Imports the datetime library

def countOccurences(item,theList):
#Defines count occurences
    occurences = 0
    #Creates occurences variable
    for i in theList:
    #Creates a for loop
        if i == item:
        #Check if i is equal to item
            occurences = occurences + 1
            #Adds 1 to occurences
    return occurences
    #Returns the value of occurence back to the main program

def total_cost(total1,total2):
    total_cost1 = total1 * 5
    #Creates the variable total_cost1 and sets it equal to total1 times 5
    total_cost2 = total2 * 10
    #Creates the variable total_cost2 and sets it equal to total2 times 10
    total_cost = total_cost1 + total_cost2
    #Creates the variable total_cost and sets it equal to total_cost1 + total_cost2
    return total_cost
	
def most_popular(School,Website):
    if Website > School:
    #Creates an if function to see if Website is more than School
        most_popular = "the website"
        #Creates a variable called most_popular and sets it to "the website"
    else:
        most_popular = "the school"
    return most_popular

total2 = 0
#Creates the total2 variable
total1 = 0
theList = []
#Creates an array

file = open("Data.csv", "r")
#Opens the csv file as readable
reader = csv.reader(file)
#Creates a variable for reading the file
file2 = open("Export.csv", "w")
for row in reader:
#Creates a for loop to repeat for every row
    if row[1] == "F3":
    #Creates an if function to see if row[1] is equal to F1
        total2 = total2 + int(row[2])
        #Makes total2 equal to total2 + the value of row[2]
        file2.write(row[0]+", "+row[1]+", "+row[2]+", "+row[3]+"\n")
        #Makes total2 equal to total2 + the value of row[2]
    elif row[1] == "F2":
        total2 = total2 + int(row[2])
        file2.write(row[0]+", "+row[1]+", "+row[2]+", "+row[3]+"\n")
    elif row[1] == "F1":
        total2 = total2 + int(row[2])
        file2.write(row[0]+", "+row[1]+", "+row[2]+", "+row[3]+"\n")
    else:
        total1 = total1 + int(row[2])
    theList.append(row[3])
    #Adds each item in row[3] to the array
file.close()
#Closes the file
file2.close()
item = "S"
#set item to S
occurences = countOccurences(item,theList)
#Uses the countOccurences function
School = occurences
#Set School to the value of occurences
item = "W"
occurences = countOccurences(item,theList)
Website = occurences
time = datetime.datetime.now()
#Creates a variable called time and uses the imported datetime to get the current date and time
year = time.year
#Creates a variable called year and sets it to the value of the current year
print("Essell Academy Choral Shield " + str(year))
#Prints text and the year variable to the screen
print("The most popular method of sales is " + most_popular(School,Website))
print("The total money raised for charity is £" + str(total_cost(total1,total2)))
