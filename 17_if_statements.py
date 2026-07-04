a = 10;

if a ==10:
    print("This is inside the if block")

x = 10;
y = 20;

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
    

c= int(input("Enter your age: "))
if c >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
    
name = input("Enter your name: ")
gender = input("Enter your gender: ")
if gender == "male":
    print("Hello Mr. " + name)
elif gender == "female":
    print("Hello Ms. " + name)
else:
    print("Invalid gender")
    

username = input("Enter your username: ")
password = input("Enter your password: ")

if(username == "admin" and password == "1234"):
    print("Welcome to the system")
elif(username == "user" and password != "1234"):
    print("Invalid password")
else:
    print("Invalid username or password")