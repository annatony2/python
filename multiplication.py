'''
author:anna tony
date 29-10-2024
python program to print multiplication table upto 12
'''
number=int(input('enter the number : '))
for i in range(1,13):
    mul=number*i
    print(f'{i}x{number}={mul}')