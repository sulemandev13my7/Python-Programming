def outer():
    print("Inside Outer function")
    
    def inner():
        print("Inside Inner Function")
    
    inner()

outer()


def calculator(a,b):
    
    def add():
        return a+b;

    def subtruct():
        return a-b;
    
    print("Addition :",add())
    print("Subtruction :",subtruct())

calculator(32,10)





def login(username,password):
    
    def validate():
        return username == "admin" and password == "123";
    
    if validate():
        print("Login Successfull");
    else:
        print("Invalid Credentional")


login("admin","123")
login("admin","1234")






def outer():
    print("Inside Outer function")
    
    message = "Welcome";
    
    def inner():
        print("Inside Inner Function")
        print(message)
    
    inner()

outer()

