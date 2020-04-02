# importing libraries
import csv
import json


# defining function for checking unofficial name
def isUnofficialName(name):
    if not name.isalpha():
        return True
    if not (any(i.isupper() for i in name)):
        return True
    return False


# creating empty list for csv data
csvList = []

# Adding CSV data to csvList
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for column in reader:
        csvList.append(column)

# printing and removing unofficial names
for csvData in csvList:
    if isUnofficialName(csvData[0]):
        print(csvData[0])
        csvData[0] = "badName0"

# Loading json file
with open('data.json') as f:
    jsonList = json.load(f)

# printing desired result
for csvData in csvList:
    if csvData[0] == "badName0":
        continue
    for jsonData in jsonList:
        if jsonData['n'] == csvData[0]:
            print("{name}, {rollno}, {branch}, {organization}, {project}".format(name=csvData[0], rollno=jsonData['i'],
                                                                                 branch=jsonData['d'],
                                                                                 organization=csvData[1],
                                                                                 project=csvData[2]))
