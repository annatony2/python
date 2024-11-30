#author Anna Tony
#date 30-1-2024
#version 1
def mobile_number():
    n=input('enter the mobile number : ')
    if len(n)==10 and n[0] in [7,8,9]:
        print('The given number is valid')
    else:
        print('The given number is invalid')
mobile_number()