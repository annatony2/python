#author Anna Tony
#date 03-12-2024
#version 1
def factorial (n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print('Factorial : ',factorial(5))