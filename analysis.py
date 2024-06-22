import csv
import math_functions as mf
import math
import matplotlib.pyplot as plt

"""
Objectives: 

Do smokers tend to have higher charges than non-smokers?
Is there a relationship between being a male or female and being a smoker or not?

    * Add results to GitHub repository

"""
    
# Picks rows (indices) from lists (columns) stored in a dictionary (where keys are headers from a csv file)
# only if the value at the index in the list passes the 'conditions' (1 or more lambda functions)
# Example: lambda a: True if a > 150 else False (results in a list of every index where the value is > 150)
def combine_data(data_dict,header,conditions):
    indices = []
    for index in range(len(data_dict[header])):
        datum = data_dict[header][index]
        passes = len(conditions)
        for func in conditions: # Itterates through the lambda function list to test the value 'datum'
            if func(datum):
                passes -= 1
        if passes == 0: # If the value at the index passes all of the conditions
            # Add the index number to the list
            indices.append(index)
    return indices

# Returns a list of all values from a list based on 'indices'
def values_from_column(data_dict,header,indices):
    values = []
    for index in indices:
        values.append(data_dict[header][index])
    print(str(len(data_dict[header])) + " --> " + str(len(values)))
    return values

# Creates a list of bins (where values falling within the bin range are counted up)
# Returns counts of values falling in each bin range, and the bin ranges themselves
# Designed to be used with:  matplotlib.plot.stairs(values=counts,edges=bin_ranges)
def count_into_bins(data_list,bin_size,max=0):
        # If max size is not manually defined, set the max to the highest value in data_list
        if max == 0:
            min,max = mf.min_max(data_list)
        # Create ranges for bins to count values into from data_list
        # (Exapmle: 1398.00 would fall into the second bin where bin_ranges = [0, 1000, 2000, 3000])
        bin_ranges = [x*bin_size for x in range(math.ceil(max/bin_size))]
        counts = [0 for bin in range(len(bin_ranges))]

        # Convert every value in 'data_list' to a float value
        for index in range(len(data_list)):
            data_list[index] = float(data_list[index])
        data_list.sort()

        for datum in data_list:
            for index in range(len(bin_ranges)):
                # If the value 'datum' is bigger than the biggest bin range, add it to the final bin.
                if datum > bin_ranges[-1]:
                    counts[-1] += 1
                    break
                elif (datum > bin_ranges[index]) and (datum < bin_ranges[index+1]):
                    counts[index] += 1
                    break
                else: 
                    continue
        bin_ranges.append(bin_ranges[-1]+bin_size)
        return counts,bin_ranges

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

    # Conditions to check for (as lambda functions to pass to the 'combine_data' function)
    is_smoker = lambda a: True if a == "yes" else False
    not_smoker = lambda a: True if a == "no" else False

    northeast = lambda a: True if a == "northeast" else False
    nortwest = lambda a: True if a == "northwest" else False
    southeast = lambda a: True if a == "southeast" else False
    southwest = lambda a: True if a == "southwest" else False

    cnt,mn,stdev,rng = mf.summary_numerical(insurance_data['charges'],"Total charges analysis:")

    # a list of indices from the smoker list where the value is 'yes'
    smokers = combine_data(insurance_data,'smoker',[is_smoker])
    smoker_charges = values_from_column(insurance_data,'charges',smokers)
    mf.summary_numerical(smoker_charges,"smoker charges analysis:")

    non_smokers = combine_data(insurance_data,'smoker',[not_smoker])
    non_smoker_charges = values_from_column(insurance_data,'charges',non_smokers)
    mf.summary_numerical(non_smoker_charges,"non-smoker charges analysis:")

    counts,bin_ranges = count_into_bins(insurance_data["charges"],1000)
    counts_smokers,bin_ranges_smokers = count_into_bins(smoker_charges,1000,max=rng[1])
    counts_non_smokers,bin_ranges_non_smokers = count_into_bins(non_smoker_charges,1000,max=rng[1])

    fig, (ax1,ax2,ax3) = plt.subplots(3,sharex=True,sharey=True)
    ax1.stairs(counts,bin_ranges)
    ax2.stairs(counts_non_smokers,bin_ranges_non_smokers)
    ax3.stairs(counts_smokers,bin_ranges_smokers)
    plt.show()
    
