number = [1,2,3,4,5,6]

square = [];

for num in number:
    square.append(num * 2)
    
print(square)


number = [1,2,3,4,5,6]
square=[num ** 2 for num in number];
print(square);


names = ["salman","usman","ayan"];
upper = [name.upper() for name in names];
print(upper);



names = ["salman","usman","ayan"];
length = [len(name) for name in names];
print(length);



number = [1,2,3,4,5,6,7,8];
evens = [num for num in number if num % 2 == 0];
print(evens)



number = [1,2,3,4,5,6,7,8];
odd = [num for num in number if num % 2 != 0];
print(odd)



text = "A1B2C3D4";
digits = [ch for ch in text if ch.isdigit()]
print(digits)


number = range(1,11);
result = [n **2 for n in number if n % 2 == 0];
print(result);



marks = [34,67,90,23,56];
status = ["Pass" if m >= 40 else "Fail" for m in marks]
print(status)



matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
];

flat = [num for row in matrix for num in row];
print(flat);


flat = [];

for row in matrix:
    for num in row:
        flat.append(num);

print(flat);



numbers=[1,2,3,4,5,5,6,7,8,9,10];

unique = {num for num in numbers}
print(unique)



numbers=[1,2,3,4,5,6,7,8,9,10];

unique = {num ** num for num in numbers}
print(unique)



tupleSquare = tuple(x ** 2 for x in range(5));
print(tupleSquare)


number=[1,2,3,4,5]

square_dict = {n: n*n for n in number}

print(square_dict)



students = ["salman","usman","ayan"]
res = {name:len(name) for name in students}
print(res)

words = ["salman","usman","ayan","salman","usman","ayan"]
frequency = {word:words.count(word) for word in set(words)}
print(frequency)


Student = [("salman", 90), ("usman", 80), ("ayan", 70)]
grade_dict = {
    name: 'A'
    if score >= 90 else 'B' 
    if score >= 80 else 'C' 
    for name, score in Student
}

print(grade_dict)


gen = (x*x for x in range(5))
print(gen)
print(list(gen))

even_gen = (x for x in range(10) if x % 2 == 0)
print(even_gen)
print(list(even_gen))

name = ["Salman","Usman","Ayan"];

upper = (n.upper() for n in name);
print(upper)
print(list(upper))