# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line
print(','.join([str(x) for x in range(2000,3201) if x%7==0 and x%5!=0]))

# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
print('Names reversed -->', str(input('Enter First Name : ') + ' ' + input('Enter Last Name : '))[::-1])
