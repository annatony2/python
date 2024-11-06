count=int(input('How many numbers do you want to enter? : '))
num=int(input('Insert the number : '))
large=num
small=num
while 1<count:
    num=int(input('Insert the number : '))
    count-=1
    if num>large:
        large=num
    elif num<small:
        small=num
print('The greatest value is :',large,'\nThe smallest value is : ',small)