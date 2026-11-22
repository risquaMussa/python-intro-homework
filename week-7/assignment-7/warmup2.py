#Warmup 2: Read a CSV with DictReader

import csv

with open("../data/students.csv", "r") as file:
    #Reads CSV rows using column names
    #eader = csv.reader(file) 
    reader = csv.DictReader(file)


    next(reader)
    for student in reader:
        print(f"{student['name']}:{student['grade']}")