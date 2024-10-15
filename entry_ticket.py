'''
author Anna Tony
date 15-10-2024
python program to determine the entry ticket fare in zoo based on age
'''
age=int(input("Enter your age : "))
if (age<10):
    print("As you are",age,"years old your ticket fare is 7 ")
elif(age>=10)and(age<60):
    print("As you are",age,"years old your ticket fare is 10 ")
else:
    print("As you are",age,"years old your ticket fare is 5 ")