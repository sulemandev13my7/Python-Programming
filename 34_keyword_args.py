def students(**kwarg):
    print(kwarg);
    
students(name="salman",age=23)


def student(**kwarg):
    print(kwarg['name']);
    
student(name="salman",age=23)



def stud(**kwargs):
 for keys, value in kwargs.items():
    print(keys,":",value);

stud(name="M.suleman",age=23,batch="MERN Stack") 



def display(*args,**kwargs):
    print("Positional Argument :");
    
    for value in args:
        print(value);
    
    print()
    
    print("Keywords Arguments :");
    
    for keys,value in kwargs.items():
        print(keys, ":", value)
    
display(1,2,3,name="Salman",age=18,batch="Python")




def demo(name,age,*skills,**details):
    print(name,age);
    
    for value in skills:
        print(value);
        
    for key,values in details.items():
        print(key,":",values);
        
demo("M.suleman",18,"No Job","No Search",address="New Muzzaffrabad Colony Landhi Krachi",road = "22#Number")