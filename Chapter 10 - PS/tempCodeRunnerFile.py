class calculator:
    def __init__ (slf, n):
        slf.n = n


    def square(slf):
        print (f"the square is {slf.n*slf.n}")

a = calculator (int(input("enter a number :")))
a.square()
