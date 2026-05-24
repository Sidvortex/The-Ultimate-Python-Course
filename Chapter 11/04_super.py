class parent():
    def __init__(self):
        print("constructor of parent")
    a=1

class child1(parent):
    def __init__(self):
        print("constructor of child1")
    b=2

class child2(child1):
    def __init__(self):
        super().__init__()                  # prints the one upper or parent class (only by one) that is why it is called super
        print("constructor of child2")
    c=3

x = parent()
print (x.a)

y = child1()
print(y.a, y.b)

z = child2()
print (z.a, z.b, z.c)

