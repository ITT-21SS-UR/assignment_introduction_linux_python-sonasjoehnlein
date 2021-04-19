import sys
import math  

arr = [] #array or list for floats
length = int(input("Please enter the range of numbers: ")) #Enter Range

for i in range(length): #Fill the list with numbers
    value = float(input("Enter the value: ")) #User input
    arr.append(value)                       # put in the list

n = len(arr) #length for median
arr.sort()   #sort the array for median

#Mean
mean=sum(arr)/len(arr) #calculate the mean
print("Mean is: " + str(mean))            # print out the mean


#Median thread found in https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
if n % 2 == 0:
    median1 = arr[n//2]
    median2 = arr[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = arr[n//2]
print("Median is: " + str(median))


#standard deviation Thread found in https://stackoverflow.com/questions/24023927/computing-standard-deviation-without-packages-in-python
var  = sum(pow(x-mean,2) for x in arr) / len(arr)  # variance
std  = math.sqrt(var)  # standard deviation
print(std)
