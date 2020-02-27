import csv
import datetime

def countOccurences(item,theList):
    occurences = 0
    for i in theList:
        if i == item:
            occurences = occurences + 1
    return occurences

def total_cost(total1,total2):
    total_cost1 = total1 * 5
    total_cost2 = total2 * 10
    total_cost = total_cost1 + total_cost2
    return total_cost
	
def most_popular(School,Website):
    if Website > School:
        most_popular = "the website"
    else:
        most_popular = "the school"
    return most_popular

total2 = 0
total1 = 0
theList = []
file = open("Data.csv", "r")
reader = csv.reader(file)
file2 = open("Export.csv", "w")
for row in reader:
    if row[1] == "F3":
        total2 = total2 + int(row[2])
        file2.write(row[0]+", "+row[1]+", "+row[2]+", "+row[3]+"\n")
    elif row[1] == "F2":
        total2 = total2 + int(row[2])
        file2.write(row[0]+", "+row[1]+", "+row[2]+", "+row[3]+"\n")
    elif row[1] == "F1":
        total2 = total2 + int(row[2])
        file2.write(row[0]+", "+row[1]+", "+row[2]+", "+row[3]+"\n")
    else:
        total1 = total1 + int(row[2])
    theList.append(row[3])
file.close()
file2.close()
item = "S"
occurences = countOccurences(item,theList)
School = occurences
item = "W"
occurences = countOccurences(item,theList)
Website = occurences
time = datetime.datetime.now()
print("Essell Academy Choral Shield " + str(time.year))
print("The most popular method of sales is " + most_popular(School,Website))
print("The total money raised for charity is £" + str(total_cost(total1,total2)))
