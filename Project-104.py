import csv
from hashlib import new
with open("height_weight.csv", newline = "") as f:
    reader = csv.reader(f)
    file_Data = list(reader)

file_Data.pop(0)

new_data = []
for i in range(len(file_Data)):
    n_num = file_Data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
total = 0
for x in new_data:
    total += x

mean = total/n
print("Mean is: " + str(mean))
