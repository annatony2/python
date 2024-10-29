'''
author:anna tony
date 29-10-2024
python program to check the given number is prime or not
'''
number=int(input('enter the number : '))
isPrime=True
for i in range (2,number):
    if number%i==0:
        isPrime=False
        break
if isPrime:
        print(f'the given number {number} is prime')
else:
    print(f'the given number {number} is not prime')