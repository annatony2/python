#author Anna Tony
#date 03-12-2024
#version 1
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
num=int(input('enter the number : '))
print('Factorial : ',factorial(num))
