import csv
from hashlib import new
from statistics import median
with open("height_weight.csv", newline = "") as f:
    reader = csv.reader(f)
    file_Data = list(reader)

file_Data.pop(0)

new_data = []
for i in range(len(file_Data)):
    n_num = file_Data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()
if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median = (median1 + median2)/2
else:
    median = new_data[n//2]
    print(n)
print("Median is: " + str(median))