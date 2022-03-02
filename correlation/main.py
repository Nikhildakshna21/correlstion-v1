import csv
import numpy as np

marks=[]
daysPresent=[]

with open('data.csv') as file:
    data = csv.DictReader(file)
    for row in data:
        marks.append(float(row['Marks In Percentage']))
        daysPresent.append(float(row['Days Present']))
    
print(np.corrcoef(marks,daysPresent)[1,0])