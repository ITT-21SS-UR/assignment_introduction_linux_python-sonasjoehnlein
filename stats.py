import sys
import math  #import math module for math.sqrt
import statistics  #import statistics module for median / standard deviation

# https://www.gutefrage.net/frage/wie-in-python-mehrere-zahlen-in-input-eingeben

numbers_input = input("Geben Sie vier Zahlen ein (durch Komma getrennt): ")
numbers_string = numbers_input.split(',')
numbers = [float(numbers_string[i]) for i in range(len(numbers_string))]
total_sum = sum(numbers)

print(total_sum)

print(math.sqrt(total_sum)) 
print(statistics.stdev(numbers))  
print(statistics.median(numbers))
