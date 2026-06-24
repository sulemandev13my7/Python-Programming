# List
# Mutable
# Allows Duplicates
# Slightly slowwer from tuple
# usecase Use a List when data may change
fruits = ["orange", "mango", "bananas","Grapes"]

print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

fruits[0:3]
print(fruits)

print(fruits[1:3]);

fruits[1] = "Apple";
print(fruits)

data = ["salman",25,75.65,True];

name,age,height,isMarried = data;
print(name,age,height,isMarried);
print(name)
print(age)
print(height)
print(isMarried)

print(data)

print(data[0])

# Tuple
# Immutable
# Allows Duplicates
# tuple fasterwwer from list
# usecase Use a Tuple when data should not change

fruits =("Apple","Orange","Mango","Banana");

print(fruits);
print(type(fruits));

print(fruits[0]);

# fruits[0]="onion";
# print(fruits);#not change

fruits = ("Apple","Mango");
veg = ("carrot","potato");

mixed =fruits+veg ;
print(mixed);

data = ('salman','age',23,23)
print(data)