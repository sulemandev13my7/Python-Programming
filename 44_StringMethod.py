a = "hello world";

print(a);
print(a[0]);
print(a[2]);

print(a[-1]);
print(a[2:5]);

print(a[:5]);

print(a[-5:]);
print(a[-5:-2]);

for i in a:
    print(i);
    

for i in "Python":
    print(i);
    

print(len(a));



# methods of string

text = "hello world";

result = text.upper();
print(result);


result = text.capitalize();
print(result);


result = text.lower();
print(result);


result = text.title();
print(result);



text = "python is a programming language. python is easy to learn. python is popular.";

print(text.find("programming"));
print(text.find("python",35));


print(text.count("a"));
print(text.count("a",20));
print(text.count("a",20,30));


print(text.startswith("python"));
print(text.startswith("programming",12));



url = "https://google.com";

print(url.startswith("https"));

if url.startswith("https"):
    print("valid url");
else:
    print("Invalid url");
    
    
if url.startswith(("https://","http://")):
    print("valid url");
else:
    print("Invalid url")
    
print(url.endswith("com"))


text = "  python is a programming  ";

print(text.strip())
print(text.lstrip())
print(text.rstrip())


text = " \t python is a programming  ";
print(text)



text = " \t\n python is a programming  ";
print(text)



text = "python is a programming";
print(text.split())


text = "python, is, a, programming";
print(text.split(","))


text = "Python Java PHP C++ Ruby Go";
print(text.split(" ",3))


fruits = ["Apple","Banana","Grapes"];
print(" ".join(fruits));
print(",".join(fruits));
print("-".join(fruits));

text = "I like Java";
print(text.replace("Java","Python"));



text = "I like Java Java Java";
print(text.replace("Java","Python",2));




print("Python123".isalnum())
print("Python 123".isalnum())
print("Python@123".isalnum())

print("Python".isalpha())
print("Python language".isalpha())


print("1324".isnumeric())



print("python".islower())
print("python langauge".islower())
print("python 1234".islower())
print("python1234".islower())


print("PYTHON".isupper())
print("PYTHON LANGAUAGE".isupper())
print("PYTHON 1234".isupper())
print("PYTHON1234".isupper())


print("PYTHON LANGAUAGE".isspace())
print(" ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\t\n".isspace())


text = "python";
print(text.center(20))
print(text.center(20,"*"))


print(text.ljust(20,"*"))
print(text.rjust(20,"*"))


number = "25";

print(number.zfill(5));


name = "John";
age = 24;

print(f"Hello {name}")
print("Hello {}".format(name))
print("Name {}, age {}".format(name,age))
print("Name: {}, age: {}".format(name,age))
print("Name: {1}, age: {0}".format(name,age))

print("{:^10}".format("Python"))
print("|{:^10}|".format("Python"))
print("|{:<10}|".format("Python"))
print("|{:>10}|".format("Python"))



std={
    "name":"suleman",
    "age":21,
    "city":"Karachi"
}

text = "{name} is {age} years old and lived in {city}"
print(text.format_map(std))