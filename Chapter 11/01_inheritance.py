class employee():
    company = "TCS"
    name = "default name"
    def show(self):
        print(f"the name of the employeee is {self.name}")

'''
class emplo():
    company = "TCS infotech"
    def show(self):
        print(f"the name is {self.name} and his language is {self.language}")
'''

class emplo(employee):
    company = "TCS infotech"
    language = "C++"
    def showlanguage(self):
        print(f"the name is {self.name} and the language is {self.language}")


a = employee()
b = emplo()
b.show()
b.showlanguage()
