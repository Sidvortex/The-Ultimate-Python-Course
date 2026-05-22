class employee:
    language = "python"
    salary = 600000
    age = 24

    def getinfo(self):
        print (f"{self.name} is assigned to {self.language}, with a salary fixated at {self.salary}LPA")


    @staticmethod
    def greet():
        print (f"{majdoor.name}, good morning")


majdoor = employee()
majdoor.name = "siddharth"   #this is a instance attribute, or you can also call it object attribute
majdoor.greet()
majdoor.getinfo()
#employee.getinfo(majdoor)    #also can be used instead the upper one