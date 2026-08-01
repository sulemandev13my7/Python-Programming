def add(a,b):
    result=a*b;
    return result;

mul=add(12,5);

print(mul);

def num(number):
    if number %2 == 0:
        return "Even";
    else:
        return "Odd";

print(num(8))


def total(number):
    result=0;
    
    for num in number:
        result += num;
    
    return result

    
marks=[1,34,60,90];

print(total(marks));