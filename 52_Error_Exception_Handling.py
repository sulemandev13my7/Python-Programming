# try:
#     num = int(input("Enter Your Number "));
    
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")

# else:
#     print(f"You entered the number: {num}")
    
# finally:
#     print("Always Executes");
    

# try:
#     f = open("testing.txt");
    
# except FileNotFoundError:
#     print("File not found Error");

# else:
#     print(f.read())
#     f.close()
    
# finally:
#     print("Program Finished");



# age = int(input("age : "));

# if age < 18:
#     raise Exception("Not Eligible");

# print("Eligible")



correct_password = "python123";

try:
    password = input("Password ");
    
    if password != correct_password:
        raise ValueError("Incorrect Password");
    
except ValueError as e:
    print(e)
    
else:
    print("Login Succesfully")