class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
s1 = Student("Salman", 20)

print(s1.name)
print(s1.age)





class Student:
    city = "Pakistan"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
s1 = Student("Salman", 20)

print(s1.name)
print(s1.age)
print(s1.city)





class Student:
    city = "Pakistan"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.marks = [80, 90, 70]
        self.address = {
            "city":"Karachi",
            "country":"Pakistan"
        }
    
s1 = Student("Salman", 20)


s1.name = "usman" 

# del s1.age

print(s1.name)
print(s1.age)
print(s1.city)
print(s1.marks)
print(s1.marks.address)
