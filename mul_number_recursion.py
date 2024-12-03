#author Anna Tony
#date 03-12-2024
#version 1
def mul_number(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mul_number(n1,n2-1)
n1=int(input('Enter number 1 : '))
n2=int(input('Enter number 2 : '))
print(n1,'X',n2, ' = ', mul_number(n1,n2))