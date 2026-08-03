def sum(a,b):
    return a+b;

print(sum(2,4))



sum = lambda a , b : a + b

print(sum(12,12));
print(sum(12,13));


square = lambda x : x * x;
print(square(4))


cube  = lambda x : x ** 3;
print(cube(3));


maximum = lambda a,b: a if a > b else b;

print(maximum(15,30));
print(maximum(15,40));





number = [2,3,3,5,3];
result = [];

for num in number:
    result.append(num * num);
    
print(result);



number = [2,3,3,5,3];
result = list(map(lambda x : x * x, number));
print(result);


num = [23,21,45,44,76];
res = filter(lambda x : x % 2 == 0,num);
print(list(res));