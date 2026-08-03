def variable(*args):
    print(args);
    
variable(1)
variable(1,243,34,34)
variable(1,243)



def number(*args):
    print(args[0]);
    
number(12,1,2)



def num(*args):
    for numb in args:
        print(numb);
    
num(10,2,30);


def total(*number):
    result = 0;
    for num in number:
        result += num;

    return result;

print(total(23,34,45))
print(total(23,34,457))




def students(*names):
    
    print("Student List");
    
    for name in names:
        print(name);
    
students("salman","usman","ayan")



def students(messege,*names):
    
    print("Student List");
    
    for name in names:
        print(messege,name);
    
students("Hello","salman","usman","ayan")
