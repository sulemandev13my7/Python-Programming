numbers = [1,2,3,4,5];

def square(n):
    return n * n;

result = map(square,numbers);

print(list(result));




names = ["salman","usman","ayan","noman"];

result = map(str.upper,names);
print(list(result))








names = ["salman","usman","ayan","noman"];

result = map(len,names);
print(list(result))




prices = [100,250,500];

def add_gst(price):
    return price + (price * 0.18)

result = map(add_gst,prices)
print(list(result))





prices = [100,250,500];
result = list(map(lambda price: price + (price * 0.18),prices))
print(result)





prices = [100,250,500];
gst=[18,12,5]
result = list(map(lambda p,g: p + (p * g/100),prices,gst))
print(result)


 
 
 
numbers=[1,2,3,4,5,6,7,8];
def even(n):
    return n % 2 == 0;
 
result = filter(even,numbers);
print(list(result))



numbers=[1,2,3,4,5,6,7,8];
def odd(n):
    return n % 2 != 0;
res = filter(odd,numbers);
print(list(res))



ages = [12,18,25,14,60];
result = filter(lambda age: age >=18,ages);
print(list(result));


words=["cat","elephent","dog","python","AI"];
result = filter(lambda word: len(word) > 3,words);
print(list(result));


emails=["salo@gmail.com","salman","admin@gmail.com","hello"];
res = filter(lambda email:"@" in email,emails);
print(list(res));


salary = [1000,180000,20000,15000,2000];
eligible = filter(lambda s: s >= 20000,salary);
bonus = map(lambda s: s+5000,eligible);
print(list(bonus));