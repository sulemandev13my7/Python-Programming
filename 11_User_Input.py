name = "M.Suleman";
city = "karachi";
print("hello my name is",name)
print("hello my city is",city)


name = input("Enter Your name :");
city = input("Enter Your city :");

print("hello my name is",name)
print("hello my city is",city)

name = input("Enter Your name :");
city = input("Enter Your city :");

print("Hello My name is ",name, end=" ")
print("I am from ",city);

name = input("Enter Your name :");
city = input("Enter Your city :");

print(f"My name is {name} and city {city}");


width = int(input("Enter width "));
height = int(input("Enter Height "))

area = width * height
print(f"Area of rectangle ={area}")
print(type(area))

width = float(input("Enter Your Width room : "));
height = float(input("Enter Your Height room : "));

area = width * height;

print(f"area of rectangular is = {area}");
print(type(area))


try:
    salary  = int(input("Enter Your salary range ... : " ))
    lastExpect  = int(input("Enter Your LastExpect ... : " ))
    total = salary * lastExpect
    print(f"Your salary is range {total} 👌⭐✅ ")
except ValueError:
    print("Please enter a valid number ")