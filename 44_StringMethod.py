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




