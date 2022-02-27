width =int(input("enter pattern width "))

for i in range(1,width+1,1): # how many lines till max width
    for j in range(i): # * how many times per line
        print('*', end = "")
    print('')

for i in range(width-1,0,-1):
    for j in range(i):
        print('*', end="")
    print('')

width =int(input("enter pattern width "))
count = 0
for i in range(2*width+1):
    count += 1
    if count <= width + 1:
        print('*' * i, count)
        j = i
    else:
        j -=1
        print("*" * j,count,j)


