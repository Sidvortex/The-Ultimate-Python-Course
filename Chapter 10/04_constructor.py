class employee:
    language = "python"
    salary = 600000
    age = 24

    def getinfo(self):
        print (f"{self.name} is assigned to {self.language}, with a salary fixated at {self.salary}LPA")


    @staticmethod
    def greet():
        print (f"{majdoor.name}, good morning")

    def __init__(self, name, age, language, salary):                 #this is dunder method, it doesn't need a call function it automatically gets called
        self.name = name
        self.age = age
        self.language = language
        self.salary = salary
        print ("this is an automatically called function")  #it gets called everytime when a new object is created 


majdoor = employee("Siddharth", 24, "python", "25")
majdoor.name = "siddharth"   #this is a instance attribute, or you can also call it object attribute
majdoor.greet()
majdoor.getinfo()
#employee.getinfo(majdoor)    #also can be used instead the upper one

#majdoor2 = employee()   #created object to call init twice