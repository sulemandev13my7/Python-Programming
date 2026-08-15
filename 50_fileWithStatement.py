# with open("students.txt","r") as f:
#     print(f.read())
    
  

  
# count = 0;  

# with open("students.txt","r") as f:
#     for line in f:
#         count += 1;
    
# print("Total line :",count)    




# student = input("Enter a Student : ");

# with open("students.txt","a") as f:
#     f.write(student + "\n");
    
# print("Saved Successfully");





with open("students.txt","r") as f:
    content = f.read();
    
with open("student1.txt","w") as distination:
    distination.write(content);

print("File Copied")    