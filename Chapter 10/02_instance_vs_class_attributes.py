class employee:
    language = "python"
    salary = 600000
    age = 24

majdoor = employee()
majdoor.name = "siddharth"   #this is a instance attribute, or you can also call it object attribute
majdoor.language = "JavaScript"  #instance attribute has higher preference than class attributes !!
print (majdoor.name, majdoor.age, majdoor.language, majdoor.salary)