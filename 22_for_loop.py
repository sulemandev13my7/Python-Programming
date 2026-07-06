# list
list = [2,3,4,5,6,7];
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])


list = [2,3,4,5,6,7];

for li in list:
    print(li);
    
# tuple
tup = (2,3,4,5,6,7);
print(tup)
for t in tup:
    print(t);
    
  
#string 
str = "Javascript";
print(str)
print(str[0])
print(str[8])

for s in str:
    print(s);
    
    
# dictionary
dic = {
    "student":"M.Suleman",
    "age":21,
    "course":"Python"
}
print(dic)
print(dic["age"])

for i in dic:
    print(i)
    
for key,value in dic.items():
    print(key,":",value)
 
 
#  list enumerate
fruits = ["apple","banana","orange"];
for i,fri in enumerate(fruits):
      print(i,fri);  
    
    
#  tuple enumerate
fruits = ("apple","banana","orange");
for i,fri in enumerate(fruits):
      print(i,fri);  
    

#  string enumerate
fruits = "apple"
for i,fri in enumerate(fruits):
      print(i,fri);  
    
    
#zip 
std=["salman","khan","usman"];
marks=[70,80,90];

for s,u in zip(std,marks):
    print(s,"score",u);
    

s = 4
for i in range(s):
    print(i)



for i in range(2,25,3):
    print(i)
    
    
for i in range(10,0,-1):
    print(i)
    
    
# even number
for num in range(0,11):
    if num % 2 == 0:
        print(num);

# 2 table print
for num in range(1,11):
    print("2 x ", num , " = " , 2 * num)
    
# 3 table print
for num in range(1,11):
    print(f" 3 x {num} = {3 * num}");
    
    
for i in range(1,6):
    print(i);
else:
    print("Loop completed")