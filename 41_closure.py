def outer():
    name="salman";
    
    def inner():
        print(name);
    
    return inner;

test = outer();
test();





def greeting(name):
    
    def say_Hello():
        print(f"Hello {name}")
    
    return say_Hello;

person = greeting("salo bahi");
person1 = greeting("salman bahi");

person()
person1()




def counter():
    count = 0;
    
    def increment():
        nonlocal count
        count += 1;
        print(count)
        
    return increment;


test = counter();
test()
test()
test()







def multiply_by(x):
    
    def multiply(y):
        return x * y;
    
    return multiply;

double = multiply_by(2);
triple = multiply_by(3);
print(double(10))
print(triple(10))

