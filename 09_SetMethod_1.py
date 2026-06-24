# Set Method in Python
# A set is an unordered collection of unique elements

#Store unique values only
#duplicates value will be removed automatically
#unordered (no indexing)
#Mutable (can add/remove items)
#can contain different data types (int, float, string, tuple, etc.)

#set method name 
# add()
# update()
# clear()
# copy()
# difference()
# discard()
# remove()
# pop()

# set operation method
# union()
# intersection()
# difference()
# difference_update()
# symmetric_difference()

#set comparision method
#issubset()
# issuperset()
#isdisjoint()
# intersection_update()

# inbuild function
# len()
# max()
# min()
# set()

x = {"HTML","CSS","JS",45,67.8,True};
print(x)
print(type(x))

number={23,23,45,6,5,7}
print(number)


data ={}
data =set()
print(data)
print(type(data))

a = {"hello","salo","apple","orange"};
for item in a:
    print(item)

x = {"apple","orange","potato"};
print("apple" in x);



fruits = {"banana","orange","oranga"};

# fruits.add("mango");

# more_fruits = {"kiwi","grapes","watermelon"};

# fruits.update(more_fruits);
# fruits.remove('banana')

# fruits.discard('lichi')

# item = fruits.pop()

# print(item)
# print(fruits.clear())

fruit = fruits.copy()
print(fruit)