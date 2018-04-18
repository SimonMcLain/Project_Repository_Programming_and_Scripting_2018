# Simon McLain 2018-04-18
# Calculate averages from columns
# Code sourced from https://stackoverflow.com/questions/25597477/python-calculate-average-for-every-column-in-a-csv-file



import csv
from collections import Counter

def average_column (csv_filepath):
    column_totals = Counter()
    with open("iris.csv","rb") as f:
       for line in f:
         a = line.split(',')
         return (a[0], a[1], a[2], a[3])
         reader = csv.reader(f)
         row_count = 0.0
         for row in reader:
            for column_idx, column_value in enumerate(row):
                try:
                    a = float(column_value)
                    column_totals[column_idx] += 
                except ValueError:
                     print ("Error -- ({}) Column({}) could not be converted to float!".format(column_value, column_idx)                    
              row_count += 1.0            

    # row_count is now 1 too many so decrement it back down
    row_count -= 1.0

    # make sure column index keys are in order
    column_indexes = column_totals.keys()
    column_indexes.sort()

    # calculate per column averages using a list comprehension
    averages = [column_totals[idx]/row_count for idx in column_indexes]
    return averages