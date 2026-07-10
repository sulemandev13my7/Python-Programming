i  =  1;
while i <= 5:
    j = 1;
    while j <= 5:
        print("*",end=" ");
        j += 1;
    print();
    i += 1;
    

num = 1;
while num <= 5:
    
    i = 1;
    while i <= 10:
        print(f"{num} X {i} = {num*i}");
        i += 1;
    
    print("-" * 20);
    num += 1;
    
board = [
    ["X","O","X"],
    ["O","x","O"],
    ["X","O","X"]
]
while i < len(board):
    j = 0;
    while j < len(board[i]):
        print(board[i][j],end=" ");
        j += 1;
    print();
    i += 1;
    

students=["salman","usman","ayan"];
marks=[{"Math":98,"science":75,"english":56},{"Math":87,"science":65,"english":54},{"Math":98,"science":75,"english":56}];

i = 0;
while i < len(students):
    print(f"Student Name: {students[i]}");
    j = 0;
    while j < len(marks[i]):
        subject = list(marks[i].keys())[j];
        score = marks[i][subject];
        print(f"{subject}: {score}");
        j += 1;
    print("-" * 20);
    i += 1;