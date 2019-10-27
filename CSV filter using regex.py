# Program to read required data from csv file using regex
import csv
import re


pattern = re.compile('Health\s\w+')
file = open('constituents_csv.csv','r',newline='')
data = csv.reader(file)

for line in data:
    i =2
    matches = re.finditer(pattern,str(line[i]))
    i+=1
    for match in matches:
        # print(match)
        print(line)