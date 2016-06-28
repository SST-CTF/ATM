# Imports
import csv
import os.path

# Setting file path
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'bank')

# Read the csv
with open(filename, 'r') as f:
    next(f) # Skips first line because they are headers
    reader = csv.reader(f)
    for row in reader:
        row = list(map(float, row))
        print row # check to see if everything is working thusfar
        if 12345 == int(row[0]):
            active = 1
        else:
            active = 1