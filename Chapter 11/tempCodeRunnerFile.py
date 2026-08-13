class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"this is the class attribute of a > {cls.a}")

e = employee()
e.a = 45
e.show()