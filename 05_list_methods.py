
fruits = ['apple','banana','cherry'];

fruits.append('grapes');
print(fruits);

fruits.insert(1,'mango');
print(fruits);

# fruits.remove('cherry')
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.clear()
# print(fruits)

# fruits.sort()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits);

# fruits.reverse()
# print(fruits)

x=fruits.copy()
print(x)

x=list(fruits);
print(x)

x=fruits[:]
print(x);


x=fruits[1:]
print(x);

x=fruits[0:2]
print(x);

veg = ["carrot","Potato","onion"];

fruits.extend(veg)
print(fruits);

x = veg.index("Potato");
print(x)

x = fruits.count('mango')
print(x)

x = len(fruits);
print(x);

number = [10,6,56];
x = len(number);
print(x)


x = max(number);
print(x)

x = min(number);
print(x)

x = max(fruits);
print(x)

x = min(fruits);
print(x)

colors = ("red","green","blue","yellow");
color_list = list(colors);
print(color_list)


color = "red";
color_list = list(color);
print(color_list)

numbers = {1,2,3,4,5,6,7,8,9};
print(list(numbers))