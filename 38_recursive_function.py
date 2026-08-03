def printNumber(n):
    
    if n > 5:
        return
    
    print(n);
    
    printNumber(n+1); 

printNumber(1)





def countdown(n):
       
    if n == 0:
        print("Done")
        return
    
    print(n);
    
    countdown(n-1);
    
countdown(5);



def factorial(n):
    if n==1:
        return 1;
    
    return n * factorial(n-1)

print(factorial(5))








def reverse(text):
    if len(text) == 0:
        return ""

    return reverse(text[1:])+ text[0]

print(reverse("Python is Good"))

