#author Anna Tony
#date 30-1-2024
#upper case and lower case count
#version 1
def upper_lower():
    string=input('enter the a string:')
    upper_count=0
    lower_count=0
    for i in string:
         if i.isupper():
             upper_count+=1
         else:
             lower_count+=1
    print('upper case count : ',upper_count)
    print('lower case count : ',lower_count)


upper_lower()
