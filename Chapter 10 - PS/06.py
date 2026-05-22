class calculator:
    def __init__ (slf, n):
        slf.n = n


    def square(slf):
        print (f"the square is {slf.n*slf.n}")

a = calculator (int(input("enter a number :")))
a.square()


# no if we change the self parameter from "self" to "slf" or "harry" it wouldn't affect anything at all.
# infact it would act the same way as the self-parameter