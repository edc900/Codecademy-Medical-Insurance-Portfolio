import csv
import numpy
import pandas
import matplotlib

"""
"""

# opens insurance.csv to the reader object to be analyzed
with open('insurance.csv',newline="") as insurance:
    reader = csv.reader(insurance, delimiter=",")
    line = 0
    for row in reader:
        if line == 10:
            break
        print(row)
        line+=1