def sum(n1):
    if n1==1:
        return n1
    else:
        return n1+sum(n1-1)
n1=int(input('enter the limit : '))
print(sum(n1))