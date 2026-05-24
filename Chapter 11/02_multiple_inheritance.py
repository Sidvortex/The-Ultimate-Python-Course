class employee():
    company = "TCS"
    name = "default name"
    def show(self):
        print(f"the name of the employeee is {self.name}")

class coder():
    language = "ruby"
    def code(self):
        print (f"the coder is assigned to {self.language} language.")


class emplo(employee, coder):
    company = "TCS infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and the language is {self.language}")



a = emplo()
a.code()
a.show()
a.showlanguage()
