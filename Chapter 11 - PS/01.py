class twodvector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def show(self):
        print (f"the vectors are {self.x}, {self.y}")

class threedvector(twodvector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print (f"the vectors are {self.x}, {self.y}, {self.z}")

a = twodvector(7, 8)
b = threedvector (6, 7, 8)
a.show()
b.show()