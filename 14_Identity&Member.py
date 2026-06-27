#identity means different location par save hai

x = [10,20,30]
y = [10,20,30]
print(x is y)

y = x
print(x is y) # because same object memory location same hai

x = 100;
y = 100;

print(x is y)

x = "python"
y = "python"
print(x is y)


x = "python"
y = "python"
print(x is not y)

#Membership operator
# check whether a value exists inside a collection
# collection means *list *tuple *string *dictionary *set
# this is work to find

numbers = [10,20,30,40];

print(20 in numbers)

print(100 in numbers)


numbers = (10,20,30,40);

print(20 in numbers)

print(100 in numbers)

str = "Python Programming";

print("Python" in str);

dic = {
    "name":"salman",
    "age":14
}
print("name" in dic);

num = [1,2,3,4];

print(1 not in num)


allowed_extension = ['.jpg','.png','.gif'];

file_name = "photo.png"
if".png" in file_name:
    print("image accepted")