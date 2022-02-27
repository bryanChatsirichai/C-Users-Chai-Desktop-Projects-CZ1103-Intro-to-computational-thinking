a = 1
b = 1

while a < 1000:
    print(a)
    b , a = a+b, b

x=1
y=1
z=1
x,y,z = x+4,x+y,z+2
print(x,y,z)
'''In a, b = b, a + b, 
the expressions on the right hand side are 
evaluated before being assigned to the left hand side. So it is equivalent to:

c = a + b
a = b
b = c'''