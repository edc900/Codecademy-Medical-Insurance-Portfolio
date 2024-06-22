import csv
import math_functions as mf
import math
import matplotlib.pyplot as plt

"""
Objectives: 
    * Add results to GitHub repository

Questions:
    Do smokers tend to have higher charges than non-smokers?

"""

# Functions for sorting and analyzing data from a dataset: 
"""
Selects rows (indices) from the dataset (stored in a dictionary where keys are headers from a csv file)
IF the value under a column passes the 'conditions' (which is tested using 1 or more lambda functions)
    (Example: lambda a: True if a > 150 else False)
"""
def combine_data(data_dict,header,conditions):
    indices = []
    data_list = data_dict[header]
    # Checks datum from every row (index) under a specifit column (header).
    for index in range(len(data_list)):
        datum = data_list[index]
        passes = len(conditions)
        for func in conditions: # Itterates through the lambda function list to test the value 'datum'
            if func(datum):
                passes -= 1
        if passes == 0: # If the value at the index passes all of the conditions ...
            # ... add the index number of the value to the list
            indices.append(index)
    return indices

# Returns a list of all values from 'data_list' based on list positions from 'indices'
def values_from_column(data_dict,header,indices):
    data_list = data_dict[header]
    values = []
    for index in indices:
        values.append(data_list[index])
    return values

"""
    Creates a list of bins (where values falling within the bin range are counted up).
    
    The function returns the range of bins, 'bin_ranges' and 'counts' of values falling in each range.
    Designed to create a histogram plot with:  matplotlib.plot.stairs(values=counts,edges=bin_ranges)
"""
def count_into_bins(data_list,bin_size,max=0):
        # If the maximum value is not manually defined: set the 'max' to the highest value in 'data_list'
        if max == 0:
            min,max = mf.min_max(data_list)

        # Exapmle: 1398.00 would fall into the 2nd bin where bin_ranges = [0, 1000, 2000, 3000]
        #   therefore, counts[1] +=1 
        bin_ranges = [x*bin_size for x in range(math.ceil(max/bin_size))]
        counts = [0 for bin in range(len(bin_ranges))]

        # Converts every value in 'data_list' to a float value
        for index in range(len(data_list)):
            data_list[index] = float(data_list[index])

        # Checks each value in 'data_list' individually, and +1 to the appropriate bin.
        for datum in data_list:
            for index in range(len(bin_ranges)):
                # If the value 'datum' is bigger than the biggest bin edge, add it to the final bin.
                if datum > bin_ranges[-1]:
                    counts[-1] += 1
                    break
                # If 'datum' is bigger than the range's start, but smaller than range's end:
                # Then the value falls in the range. counts += 1 at the current bin's index
                elif (datum > bin_ranges[index]) and (datum < bin_ranges[index+1]):
                    counts[index] += 1
                    break
                else: # If 'datum' is bigger than the edges of the current range, check the next range.
                    continue
        # plt.stairs expects:  len(edges) = len(values) + 1
        bin_ranges.append(bin_ranges[-1]+bin_size) # Simply adds one more bin edge to 'bin_ranges' at the end
        return counts,bin_ranges

# Opens insurance.csv from the working directory.
file = 'insurance.csv'
with open(file,newline="") as insurance:
    reader = csv.reader(insurance, delimiter=",")

    insurance_data = {} # An empty dictionary for sorting the csv data by column.
    line = 0
    for row in reader: 
        # Each 'row' has data in this order: [age, sex, bmi, children, smoker, region, charges]
        if line == 0: # The 1st line of insurance.csv contains the column header names.
            for header in row: 
                insurance_data[header] = []

        else: # Every subsequent line in insurance.csv contains data from the subjects.
             headers = list(insurance_data.keys())
             for index in range(len(row)):
                 insurance_data[headers[index]].append(row[index])
        line+=1
    print("\nProcessed " + file + " which had " + str(line - 1) + " rows.\n")
    
    """
        The 'insurance_data dictionary' should now be in a dataframe-ready format (if the Pandas library was being used):
        The headers from the csv file are now the keys in 'insurance_data'
        and the data from each row are stored in ordered lists representing each column.
    """

    # Conditions to check for (as lambda functions to pass to the 'combine_data' function)
    is_smoker = lambda a: True if a == "yes" else False
    not_smoker = lambda a: True if a == "no" else False


    # Statistical Analysis of the insurance.csv data:

    # ENTIRE SAMPLE:
    cnt,mn,stdev,rng = mf.summary_numerical(insurance_data['charges'],"Total charges analysis:")
        # Prints N, mean, standard dev., and the min/max for insurance charges entire sample.
    counts,bin_ranges = count_into_bins(insurance_data["charges"],1000)
        # Counts values from the distribution of insurance charges into bins (to display as hisogram)

    # SMOKERS in the sample:
    smokers = combine_data(insurance_data,'smoker',[is_smoker])
        # A list of indices where the subject is a smoker
    smoker_charges = values_from_column(insurance_data,'charges',smokers)
            # A list of Insurance charges for smokers in the dataset
    cnt_smk,mn_smk,stdev_smk,rng_smk = mf.summary_numerical(smoker_charges,"smoker charges analysis:")
    smokers_and_charges = []
        # Prints N, mean, standard dev., and the min/max for insurance charges of smokers in the dataset
    counts_smokers,bin_ranges_smokers = count_into_bins(smoker_charges,1000,max=rng[1])
        # Counts values from the distribution of the insurance charges of smokers into bins (to display as hisogram)

    # NON-SMOKERS in the sample
    non_smokers = combine_data(insurance_data,'smoker',[not_smoker])
        # A list of indices where the subject is a smoker
    non_smoker_charges = values_from_column(insurance_data,'charges',non_smokers)
        # A list of Insurance charges for smokers in the dataset
    cnt_nsmk,mn_nsmk,stdev_nsmk,rng_nsmk = mf.summary_numerical(non_smoker_charges,"non-smoker charges analysis:")
        # Prints N, mean, standard dev., and the min/max for insurance charges of non-smokers in the dataset
    counts_non_smokers,bin_ranges_non_smokers = count_into_bins(non_smoker_charges,1000,max=rng[1])
        # Counts values from the distribution of insurance charges of non-smokers into bins (to display as histogram)

    
    # Plotting data using matplotlib:

    fig, (ax1,ax2,ax3) = plt.subplots(3,sharex=True,sharey=True)
    fig.suptitle("Comparing insurance charges\n",size=15)
    fig.tight_layout()

    ax1.stairs(counts,bin_ranges)
    ax1.title.set_text("Charges among everyone in the sample")

    ax1.vlines(mn,0,100,color="red") # Red line at the mean of the total sample's insurance charges
    ax1.vlines(mn-(stdev*2),0,100,color="blue") # blue lines at +/- 2 times the stdev
    ax1.vlines(mn+(stdev*2),0,100,color="blue")

    ax1.annotate("$ "+str(round(mn,2))+"\n± "+str(round(stdev,2)),xy=(mn+1000,80),color="red",size=8)

    ax2.stairs(counts_non_smokers,bin_ranges_non_smokers)
    ax2.title.set_text("Charges among non-smokers")

    ax2.vlines(mn_nsmk,0,100,color="red") # Red line at the mean of the non-smokers' insurance charges
    ax2.vlines(mn_nsmk-(stdev_nsmk*2),0,100,color="blue") # blue lines at +/- 2 times the stdev
    ax2.vlines(mn_nsmk+(stdev_nsmk*2),0,100,color="blue") 

    ax2.annotate("$ "+str(round(mn_nsmk,2))+"\n± "+str(round(stdev_nsmk,2)),xy=(mn_nsmk+1000,80),color="red",size=8)

    ax3.stairs(counts_smokers,bin_ranges_smokers)
    ax3.title.set_text("Charges among smokers")

    ax3.vlines(mn_smk,0,100,color="red") # Red line at the mean of the smokers' insurance charges
    ax3.vlines(mn_smk-(stdev_smk*2),0,100,color="blue") # blue lines at +/- 2 times the stdev
    ax3.vlines(mn_smk+(stdev_smk*2),0,100,color="blue") 

    ax3.annotate("$ "+str(round(mn_smk,2))+"\n± "+str(round(stdev_smk,2)),xy=(mn_smk+1000,80),color="red",size=8)
    plt.savefig("smoker_charge_comparision.png")
    
