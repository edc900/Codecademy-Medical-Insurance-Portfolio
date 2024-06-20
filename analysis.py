import csv
import matplotlib

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



def categorize(data_list,categories,conditions):
    group = []
    for row in data_list:
        for category in range(len(categories)):
            continue
    return group



# opens insurance.csv to the reader object to be analyzed
with open('insurance.csv',newline="") as insurance:
    reader = csv.reader(insurance, delimiter=",")

    # Creates an empty dictionary for sorting the csv data by column.
    insurance_data = {}

    # Iterates through each row of the csv file.
    line = 0
    for row in reader:
        # For the first row of the csv file (which will be the headers): 
        #   make the header a key in the insurance_data dictionary,
        #   and initialize the key with an empty list (for storing data from each column).
        if line == 0:
            for header in row:
                insurance_data[header] = []
        
        # For every row of data:
        #   find the key associated with the column in the insurance_data dictionary,
        #   and append the data to the empty list associated with the header key.
        else:
             headers = list(insurance_data.keys())
             for index in range(len(row)):
                 insurance_data[headers[index]].append(row[index])
        line+=1
    
    # The insurance_data dictionary should now be in a dataframe-ready format (if we were using the Pandas library):
    #   The headers from the csv file are now the keys in the insurance_data dictionary,
    #   and the data from each row in insurance.csv are stored in indexed lists for each header key

    

    print(insurance_data.keys())
    