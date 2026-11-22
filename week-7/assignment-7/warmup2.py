#Warmup 2: Read a CSV with DictReader

import csv

with open("../data/students.csv", "r") as file:
    #Reads CSV rows using column names
    reader = csv.reader(file) 


    next(reader)
    for student in reader:
        print(f"{student[0]}:{student[2]}")