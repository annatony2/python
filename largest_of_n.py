"""
author: Anna Tony
Version 1.1
Date: 27/10/2024
Python program to find the largest of n numbers
"""
count=int(input('How many numbers do you want to enter? : '))
largest= int(input('Insert the number : '))
while 1<count:
    Insert_number=int(input('Insert the number : '))
    count-=1
    if Insert_number>largest:
        largest=Insert_number
print('The greatest value is:',largest)