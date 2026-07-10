
for i in range(5):
    for j in range(5):
        print("*",end=" ");
    print()
    
rows=10;
col=10;
num=1;

for i in range(rows):
    for j in range(col):
        print(num,end=" ");
        num += 1;
    print()
    

for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
    
    
students=["salman","usman","ayan"];
marks=["math","science","english"];

for stud in students:
    print(f"\nmarks in {stud}");
    for mark in marks:
        print(mark);
        
        
students=["salman","usman","ayan"];
marks=[{"Math":98,"science":75,"english":56},{"Math":87,"science":65,"english":54},{"Math":98,"science":75,"english":56}];

for stud,m in zip(students,marks):
    print(f"\nmarks in {stud}");
    for mk,mks in m.items():
        print(f"{mk}:{mks}");