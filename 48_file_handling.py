f = open("students.txt", "r");


# print(f.read());
# print(f.read(5));
# print(f.readline());
# print(f.readline(),end="");
# print(f.readlines());

for line in f:
    print(line.strip());
    
    
f.close();