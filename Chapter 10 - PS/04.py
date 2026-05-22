class calculator:
    def __init__ (self, n):
        self.n = n
    
    @staticmethod
    def greet():
        print("hello user :)")

    @staticmethod
    def greet2():
        print("Bye user ;)")

    def square(self):
        print (f"the square is {self.n*self.n}")
    
    def cube(self):
        print (f"the cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print (f"the squareroot is {self.n**(1/2)}")

a = calculator (int(input("enter a number :")))
a.greet()
a.square()
a.cube()
a.squareroot()
a.greet2()