# def decorator(func):
    
#     def wrapper():
#         print("Before");
        
#         func();
        
#         print("After");
        
#     return wrapper;

# # best method
# @decorator
# def hello():
#     print("Hello");
    
# hello()


# old method
# def hello():
#     print("hello");
    
# test = decorator(hello)
# test()








# def decorator(func):
    
#     def wrapper(name):
#         print("Before");
        
#         func(name);
        
#         print("After");
        
#     return wrapper;

# @decorator
# def hello(name):
#     print("Hello",name);

# hello("salman")







def decorator(func):
    def wrapper(*args,**kargs):
        print("Starting....");
        
        result = func(*args,**kargs);
    
        print("Finished....");
        
        return result
        
    return wrapper;

@decorator
def add(a,b):
    return a * b
    
print(add(2,5))







logged_in = True;

def login_required(func):
    
    def wrapper():
        if logged_in:
            func();
        else:
            print("Please login");
    
    return wrapper

@login_required
def dashboard():
    print("Welcome to dashboard");
    
dashboard();



def star(func):
    
    def wrapper():
        print("********");
        func();
        print("********");
    
    return wrapper;


def welcome(func):
    
    def wrapper():
        print("Welcome");
        func();
        
    return wrapper;

@star
@welcome
def hello():
    print("Hello");
    
hello()