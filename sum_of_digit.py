'''
author Anna Tony
date 15-10-2024
python program to find sum of digit of a number
'''
number=int(input("Enter a number : "))
num=number
sum=0
while number>0:
    r=number%10
    number=number//10
    sum=sum+r
print("Sum of digit of the number",num,"is",sum)


