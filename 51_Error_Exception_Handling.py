# if 5 > 2
#     print("Hello") #syntaxError


# if 5 > 2:
#     printt("Hello") # NameError


# print(5 /0) #ZeroDivisionError: division by zero


# length = 10;
# width = 5;

# area = length + width;
# print(area) # logical error


# num = int(input("Enter Number.."));
# print(num) #num mein sirf number do gy agar string pass kiya tu ValueError: invalid literal for int() with base 10: 'hg' so this is Exception error
 
 
 

# try:
#     num = int(input("Enter Your Number"));
#     print(num);
# except:
#     print("Something went wrong");
    
    
    
# try:
#     num = int(input("Enter Your Number"));
#     print(100/num);

# except ZeroDivisionError:
#     print("Can't divide by Zero");

# except ValueError:
#     print("Invalid value")
    
# except:
#     print("Some thing went wrong");




# try:
#     num = int(input("Enter Your Number "));
#     print(100/num);
# except (ZeroDivisionError,ValueError):
#     print("Invalid value");
    
# except:
#     print("Some thing went wrong");
    

try:
    num = int(input("Enter Number : "));
    print(100/num);
except ZeroDivisionError as e:
    print("Error : " + e);
except ValueError as e:
    print(e);
    
except Exception as e:
    print("some thing went wrong",e);
    