# we can not modify
fruit = ("apple","orange","banana","orange");
print(fruit);
print(fruit.count("orange"));

# implicet tuple
x = "Html", "CSS","JS",10,20,45.23;
print(x[1]);
print(x[1:3])

nested_tuple = ((10,20),(30,40),(50,60))
print(nested_tuple)
print(nested_tuple[1])
print(nested_tuple[1][1])


fruits = ("apple","banana","orange","apple");
x = fruits.index("apple");
x = fruits.index("apple",1);
print(x);


number = (1,2,4,5,8,9,0,7);

x = number.index(5)
x = max(number)
x = min(number)
x = len(number)
print(x)


numbers = [1,2,4,5,8,9,0,7];
t = tuple(numbers);
print(t)

str = "salman";
t = tuple(str);
print(t)

r=range(5)
t = tuple(r);
print(t)