student = {
    "name":"salman",
    "fname":"M.Jan",
    "marks":98,
    "age":20,
    "skills":["python","java","c++"]    

}
print(student["name"]);
print(student.get("name"));
print(student.get("agea","not found"))

print(student.keys())
print(list(student.keys()))
print(list(student.items()))

for keys,value in student.items():
    print(keys," : ",value)

keys = ["name","age","city"];
data = dict.fromkeys(keys);
print(data);

keys = ['name','Fname','Lname','Class'];

data = dict.fromkeys(keys,'unknown');
print(data);

students = {
    'name':'M.Suleman',
    'age':23,
    'class':'MERN Stack'
}
students.pop('name')
print(students)

print(students.popitem())#last waly key - value ko remove karta hai

students.clear()
print(students)

student = {
    'name':"M.Suleman",
    'age':20,
    'city':'Karachi'
}
student.update({'name':'Salman'})
student.update({'marks':78})
print(student)

new = student.copy();
print(new);

student.setdefault("gender","Unknown");
print(student);


print(len(student))

x = str(student)
print(x)
print(type(x))