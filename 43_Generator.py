
def number():
    return [1,2,3];

print(number());




def test():
    yield "first"
    yield "second"
    yield "third"

g= test()

print(next(g))
print(next(g))





def fruit():
    yield 1
    yield 1
    yield 1

f = fruit()

print("message")

print(next(f))






def fruits():
    yield "Apple"
    yield "Orange"
    yield "mango"
    yield "grapes"

for i in fruits():
    print(i);





def square(n):
    
    for i in range(1,n + 1):
        yield i * i;
        
for value in square(5):
    print(value);