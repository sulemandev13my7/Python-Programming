class calculation:
     def sum(self,a,b):
         print(a+b);
    
     def sub(self,a,b):
        print(a-b);
       
a = calculation();
a.sum(2,3);
a.sub(2,3);


# constructor

class calculation:
    def __init__(self,a,b):
        self.a = a;
        self.b = b;
    def sum(self):
        print(self.a + self.b)
    def sub(self):
        print(self.a - self.b)
        
a = calculation(10,20);
a.sum()




# destructuring

class student:
    def __init__(self,name):
        self.name = name;
        print("Object created");
        
    def __del__(self):
        print("Object destroyed");
        
Student = student("salman");

print("program Contiues...");        





class student:
    def __init__(self,name):
        self.name = name;
        print("Object created");
        
    def __del__(self):
        print("Object destroyed");
        
Student = student("salman");

del Student

print("program Contiues...");        
