def greet():
     message="Hello";
     
     print(message);
     
greet()
# because local scope
# print(message)




count = 10;

def display():
    print(count);
    
display()
print(count)





# count = 10;

# def display():
#     count = count+1;
#     print(count);
    
# display()
# print(count)





# count = 10;

# def display():
#     count = 12;
#     print(count);
    
# display()
# print(count)





count = 10;

def display():
    global count
    count = 12;
    print(count);
    
display()
print(count)




def outer():
    number = 10;
    
    def inner():
        print(number);
    
    inner()
    
outer()




def outer():
    number = 10;
    
    def inner():
        nonlocal number
        number = number +1;
        print(number);
    
    inner()
    
outer()
outer()
outer()
