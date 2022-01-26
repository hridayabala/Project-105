import math
import csv

with open('data.csv', newline = '')as f:
    reader = csv.reader(f)

    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0

    for x in data :
        total += int(x)
    
    mean = total/n

    return mean

squared_list = []

for number in data:
    s = int(number) - mean(data)
    s = s**2
    
    squared_list.append(s)

sum = 0

for a in squared_list:
    sum = sum + a

result = sum/(len(data) - 1)

standard_deviation = math.sqrt(result)

print(standard_deviation)