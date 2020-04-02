from bs4 import BeautifulSoup
import requests
import csv

url = input("Enter url:")
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")  #getting HTML response

# Creating Empty list for data
contentArr = []

#parsing through HTML for list items
mainSection = content.find('main')
unorderedList = mainSection.find('ul')
tabArray = unorderedList.find_all('li')

#Storing data in list
for tab in tabArray:
    firstDiv = tab.findAll('div')
    cardObject = {
            "name": tab.find('a').text,
            "organization": firstDiv[0].findAll('div')[1].text.split(" ", 1)[1],
            "project": firstDiv[0].findAll('div')[0].text
        }
    contentArr.append(cardObject)


# Exporting data to csv file "data.csv"
csv_file = "data.csv"
csv_columns = ['name', 'organization', 'project']
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        #uncomment this line if we also want Column names in CSV file
        #writer.writeheader()
        for data in contentArr:
            writer.writerow(data)
except IOError:
    print("I/O error")
