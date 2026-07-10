for i in range(1,11):
    if i == 5:
        continue;
    print(i)


for i in range(1,11):
    if i %2 == 0:
        continue;
    print(i)
    
li = ['salman','ayan',"",'shif'];    
for name in li:
    if name == "":
        continue;
    print(name)
    
marks = [56,67,87,98,90];
for mark in marks:
    if mark < 80:
        continue;
    print(mark) 
    

word = "PYTHON";
for letter in word:
    if letter in "AEIOU":
        continue;
    print(letter);
    
age = 18;
if age >= 18:
    pass
print("You are eligible");

number = [8,9,10];
for num in number:
    if num == 9:
        pass;
    print(num)