# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line
print(','.join([str(x) for x in range(2000,3201) if x%7==0 and x%5!=0]))

# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
print('Names reversed -->', str(input('Enter First Name : ') + ' ' + input('Enter Last Name : '))[::-1])

# 3. Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 * π * r 3
import math
print('Volume of sphere with diameter 12 cm is {} cubic centimeter'.format((4/3)*math.pi*(12/2)**3))

# 4. Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum
(lambda a,b : a+b if a*b > 1000 else a*b)(int(input("Enter 1st number: ")),int(input("Enter 2nd number: ")))

# 5. Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
print('\n'.join([str([x for x in range(10)][i+1] + [x for x in range(10)][i]) for i in range(10-1)]))

# 6: Given a string, display only those characters which are present at an even index number.
print("Even index chars : ", input('Enter the string: ')[2::2])

# 7: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
print("Even index chars : ", input('Enter the string: ')[:int(input('Enter n: '))])

# 8: Given a list of numbers, return True if first and last number of a list is same
lst=[int(x) for x in input('Enter list of numbers delimited by comma: ').split(',')]
print('First & Last number matching ? ',lst[0]==lst[-1])
