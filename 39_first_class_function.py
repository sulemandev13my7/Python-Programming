def greet():
    print("Hello");

message = greet;
message()


print(type(message))




def add():
    print("Addition");

def subtruct():
    print("Subtruction");
    
def multiply():
    print("Multiplication");

operations = [add,subtruct,multiply];

for operation in operations:
    operation();
    
    
    
    
    
    

def add():
    print("Addition");

def subtruct():
    print("Subtruction");
    
def multiply():
    print("Multiplication");
    
operation = {
    "add":add,
    "subtruct":subtruct,
    "multiply":multiply
}

operation["add"]()

items = (10,"python",add,subtruct)
items[2]()
items[3]()

print(items[0])





def greet():
    print("Good Morning");

def execute(function):
    function()

execute(greet)




def add(a,b):
    return a+b;

def subtruct(a,b):
    return a-b;

def calculator(operation,x,y):
    return operation(x,y)

print(calculator(add,10,20))
print(calculator(subtruct,20,20))