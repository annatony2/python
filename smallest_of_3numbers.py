'''
author Anna Tony
date 15-10-2024
python program to determine the smallest of three numbers
'''
num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))
num3=int(input("Enter 3rd number : "))
if(num1<num2)and(num1<num3):
    print(num1,"is the smallest")
elif(num2<num3):
    print(num2,"is the smallest")
else:
    print(num3,"is the smallest")