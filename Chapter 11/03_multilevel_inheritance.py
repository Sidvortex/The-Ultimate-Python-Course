class parent():
    a=1

class child1(parent):
    b=2

class child2(child1):
    c=3

x = parent()
print (x.a)

y = child1()
print(y.a, y.b)

z = child2()
print (z.a, z.b, z.c)

