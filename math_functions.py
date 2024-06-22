import math

"""
    These are the functions in this script for analyzing the properties of values in a data list:
        mean(data_list)
        min_max(data_list)
        median(data_list)
        std_deviation(data_list)
        unique_values(data_list)
        summary_numerical(data_list,name)
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

# Returns the median of numerical data in a column.
def median(data):
    count = len(data)
    data_list = data # Creates a "proxy" for the 'data' list so that 'data' does not become sorted.
    data_list.sort()
    if count % 2 == 0: # for an even number of values, median is the mean of the middle 2 values
        index = int(count/2) # example: len([1,2,3,4,5,6]) / 2  -->  6 / 2  -->  3
        med = (float(data_list[index-1]) + float(data_list[index])) / 2
    else: # for an odd number of values, the median is the middle value
        index = math.floor(count/2) # example: [1,2,3,4,5,6, 7 ,8,9,10,11,12,13]  -->  math.floor(7/2)  -->  4
        med = float(data_list[index])
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
def unique_values(data_list):
    values = []
    for row_datum in data_list:
        if not (row_datum in values):
            values.append(row_datum)
    values.sort()
    return values

def summary_numerical(data_list,name="the data list:"):
    cnt = len(data_list)
    mn = mean(data_list)
    stdev = std_deviation(data_list)
    rng = min_max(data_list)
    print("From "+name)
    print("There are "+ str(cnt) + " values.")
    print("The mean is: " + str(mn))
    print("The standard deviation is: " + str(stdev))
    print("The range is: " + str(rng)+"\n")
    return cnt,mn,stdev,rng
    