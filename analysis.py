import csv
import math
import matplotlib.pyplot as plt
import numpy as np

"""
Objectives: 
    * Create a function to sort subjects into lists based on an attribute (example: all smokers, all males)
    * Create a function to return summary statistics for a list of subjects from a category 
    * Come up with attempts to answer and think of questions from the dataset

Is there a difference between male and female subjects for being a smoker?
Do smokers tend to have higher BMIs than non-smokers?
How does age relate to whether someone is a smoker or not?

    * Use matplotlib to create visuals for the data representing each question
    * Add results to GitHub repository

"""
# Returns the average value from numerical data in a column.
def mean(data_list):
    total = 0
    count = len(data_list)
    for datum in data_list:
        total += round(float(datum))
    return round(total / count, 2)

# Returns a tuple (min, max) from numerical data in a column.
def min_max(data_list):
    min = math.inf
    max = 0
    for datum in data_list:
        datum = float(datum)
        if datum < min:
            min = datum
        if datum > max:
            max = datum
    return (min,max)

def median(data_list):
    count = len(data_list)
    data_list.sort()
    if count % 2 == 0:
        index = math.floor(count/2)
        med = (float(data_list[index-1]) + float(data_list[index])) / 2
    else:
        index = math.ceil(count/2)
        med = float(data_list[index-1])
    return med

# Returns the standard deviation from numerical data in a column.
def std_deviation(data_list):
    count = len(data_list)
    avg_value = mean(data_list)
    total = 0
    for datum in data_list:
        dif_sqr = (float(datum) - avg_value)**2
        total += dif_sqr
    return (total / (count - 1)) ** 0.5

# Returns a list of unique values under one column
def unique_values(data_dict,header):
    values = []
    for row_datum in data_dict[header]:
        if not (row_datum in values):
            values.append(row_datum)
    values.sort()
    return values

# Picks rows to be returned in the 'group' list based on conditions.
def sort_rows(data_dict,header,condition):
    group = []
    for row in data_dict[header]:
        for category in range(len(1)):
            continue
    return group


# Opens insurance.csv from the working directory.
with open('insurance.csv',newline="") as insurance:
    # Points the 'reader' object to the content of insurance.csv
    reader = csv.reader(insurance, delimiter=",")

    # Creates an empty dictionary for sorting the csv data by column.
    insurance_data = {}

    # Goes through each row of the csv file.
    line = 0
    for row in reader:
        # Makes each of the headers into a key in the insurance_data dictionary.
        if line == 0:
            for header in row:
                insurance_data[header] = []
        
        # Appends the data from columns (in each csv row) to the list associated with the header key in insurance_data.
        else:
             headers = list(insurance_data.keys())
             for index in range(len(row)):
                 insurance_data[headers[index]].append(row[index])
        line+=1
    
    # The insurance_data dictionary should now be in a dataframe-ready format (if the Pandas library was being used):
    #   The headers from the csv file are now the keys in the insurance_data dictionary,
    #   and the data from each row in insurance.csv are stored in indexed lists for each header key (row 1 is indexed at 0, and so on).


    # print("unique ages:")
    # print(unique_values(insurance_data,"age"))

    # print("unique sexes:")
    # print(unique_values(insurance_data,"sex"))

    #print("unique numbers of children:")
    #print(unique_values(insurance_data,"children"))

    #print("unique smokers:")
    #print(unique_values(insurance_data,"smoker"))
    print(mean(insurance_data['charges']))
    print(std_deviation(insurance_data['charges']))
    print(median(insurance_data['charges']))
    print(min_max(insurance_data['charges']))
    
