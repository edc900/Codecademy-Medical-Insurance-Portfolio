import csv
import math_functions as mf
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
    print(mf.mean(insurance_data['charges']))
    print(mf.std_deviation(insurance_data['charges']))
    print(mf.median(insurance_data['charges']))
    print(mf.min_max(insurance_data['charges']))
    
