#author Anna Tony
#date 30-1-2024
#version 1
def triangle():
    lst=[]
    side_1=int(input('Enter the side1 : '))
    side_2=int(input('Enter the side2 : '))
    side_3=int(input('Enter the side3 : '))
    lst.append(side_1)
    lst.append(side_2)
    lst.append(side_3)
    lst.sort()
    hyp=lst[2]
    base=lst[0]
    height=lst[1]
    if hyp**2==base**2+height**2:
        print('right angle triangle ')
    else:
        print('not right angle triangle ')



triangle()