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

# opens insurance.csv to the reader object to be analyzed
with open('insurance.csv',newline="") as insurance:
    reader = csv.reader(insurance, delimiter=",")
    line = 0
    for row in reader:
        if line == 10:
            break
        print(row)
        line+=1