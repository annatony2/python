'''
author Anna Tony
date 15-10-2024
python program to determine the largest of two numbers
'''
num1=int(input("enter a number : "))
num2=int(input("enter another number : "))
if(num1>num2):
    print(num1,"is greater than",num2)
elif(num1<num2):
    print(num2,"is greater than",num1)
else:
    print("The given numbers are equal")