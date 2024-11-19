#author:Anna Tony
#date:19/11/2024
limit=int(input('Enter the limit: '))
print("\nIncreasing Triangle")
for i in range(limit+1):
  for j in range(i):
    print('*',end=" ")
  print()
print("\nDecreasing Triangle\n")
for i in range(limit,0,-1):
  for j in range(i):
    print('*',end=" ")
  print()
print("\nHill Pattern\n")
for i in range(1,limit+1):
    for j in range(limit-i):
        print(' ',end=" ")
    for k in range(2*i-1):
        print('*',end=' ')
    print()
print("\nReverse Hill Pattern\n")
for i in range(limit,0,-1):
    for j in range(limit-i):
        print(' ',end=" ")
    for k in range(2*i-1):
        print('*',end=' ')
    print()

