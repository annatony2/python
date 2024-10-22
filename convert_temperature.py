"""
author: Anna Tony
Version 1.1
Date: 22/10/2024
Python program to convert temperature values back and forth between Celsius and Fahrenheit
"""
temp=int(input("Enter temperature: "))
type=input("Is this in (C)elsius or (F)ahrenheit ? ")
final_temp=0
if type=='C':
    final_temp=(9/5*temp)+32
    print(temp," Celsius is ",final_temp," Fahrenheit.")
else:
    final_temp=5/9*(temp-32)
    print(temp," Fahrenheit is ",final_temp,"Celsius.")

