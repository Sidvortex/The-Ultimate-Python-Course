class Programmer:
    company = "Microsoft Co. Ltd."
    department = "Backend Dev."

    def getinfo(self):
        print (f"{self.name}, aged {self.age} with skills - {self.skills}; is assigned at a salary of {self.salary}LPA, at {self.company} under the position of {self.department}")


    def __init__(self, name, age, skills, salary):   #this is dunder method, it doesn't need a call function it automatically gets called
        self.name = name
        self.age = age
        self.skills = skills
        self.salary = salary
        print ("--------")  #it gets called everytime when a new object is created 


majdoor1 = Programmer("sid", 24, "Python, ML, DL, Calculus", "20",)
majdoor1.getinfo()

majdoor2 = Programmer("ayush", 24, "Python, ML, DL", "15",)
majdoor2.getinfo()

majdoor3 = Programmer("vinayak", 24, "Python, Calculus", "8",)
majdoor3.getinfo()