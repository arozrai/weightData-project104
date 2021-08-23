import csv
from collections import Counter

f = open("height-weight.csv",newline = "")
data = csv.reader(f)

file_data = list(data)

# removed title of the csv file
file_data.pop(0)

emptyArray = []

# collected height in the array
for i in range(len(file_data)):
    num = file_data[i][2]
    emptyArray.append(float(num))

#Calculating Mode 
data = Counter(emptyArray) 
mode_data_for_range = { 
    "70-110": 0, 
    "110-150": 0, 
    "150-180": 0 
} 

for weight, occurence in data.items(): 
    if 70 < float(weight) < 110: 
        mode_data_for_range["70-110"] += occurence 

    elif 110 < float(weight) < 150: 
        mode_data_for_range["110-150"] += occurence 

    elif 150 < float(weight) < 180: 
        mode_data_for_range["150-180"] += occurence 

mode_range, mode_occurence = 0, 0 

for range, occurence in mode_data_for_range.items(): 
    if occurence > mode_occurence: 
        mode_range,mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence 

mode = float((mode_range[0] + mode_range[1]) / 2) 
print(f"Mode is -> {mode:2f}")

n = len(emptyArray) 

emptyArray.sort() 
# using floor division to get the nearest number whole number 
# floor division is shown by // 
if n % 2 == 0: 
    #getting the first number 
    median1 = float(emptyArray[n//2])

    #getting the second number 
    median2 = float(emptyArray[n//2 - 1]) 

    #getting mean of those numbers 
    median = (median1 + median2)/2 
else:
    median = emptyArray[n//2] 

print("Median is: " + str(median))

# to find total number of heights
n = len(emptyArray) 
total = 0 

# adding all heights
for x in emptyArray: 
    total += x 

# finding mean
mean = total / n 
print("Mean / Average is: " + str(mean))