import math

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