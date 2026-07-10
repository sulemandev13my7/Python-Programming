for i in range(1,11):
    if i == 5:
        break;
    print(i);
    
print("Loop Finished")


fruits = ["Apple","orange","grapes","banana"];

search = "banana";

for fruit in fruits:
    if fruit == search:
        print("Fruit Found")
        break;
    
print("Search Completed")



fruits = ["Apple","orange","grapes","banana"];

search = "mango";

for fruit in fruits:
    if fruit == search:
        print("Fruit Found")
        break;
else:
    print("Not Found");
        
        
print("Search Completed");


correct_Pin = "1234";

while True:
    pin = input("Enter PIN: ");
    if pin == correct_Pin:
        print("Login SuccessFully");
        break;
    print("Incorrect PIN");