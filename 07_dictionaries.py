# Dictionary
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Creating a dictionary
#key must be unique
#key can be strings, numbers, tuples etc
#values can be of any data type
#Dictionary are mutable(changeable)
#Access values using keys

student = {
    "name": "M.Suleman",
    "age": 30,  
    "city": "New York",
    "marks":34.76,
    "passed":True,
    "skills":['python','javascript','react']
}
print(student)
print(type(student))

x = student["name"]
print(x)

print(student["age"])

student["gender"] = "male";
print(student)


print(student["skills"])
print(student[["skills"][0]])

students = dict();
print(students)



dict = dict(
    name="Sir Salman",
    age=18
);
print(dict)

student1 = {
    "student01":{
        "name":"Salman",
        "age":20
    },
    "student02":{
        "name":"khan",
        "age":18
    }
}
print(student1)
print(student1["student01"])
print(student1["student01"]["name"])

student12 = {
    "name":"salman",
    "fname":"M.Jan",
    "marks":98
}
for value in student12.values():
    print(value)


student123 = {
    "name":"salman",
    "fname":"M.Jan",
    "marks":98
}
for key,value in student12.items():
    print(key,": ",value)


student1234 = {
    "name":"salman",
    "fname":"M.Jan",
    "marks":98
}
if "name" in student1234:
    print("key Found")