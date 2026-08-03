num = "100";
print(int(num) + 1)

num = "100";
print(type(num))
print(int(num))
print(type(int(num)))
print(int(num)+1)
print(type(int(num)+1))


num = 99.99
print(int(num))

num = True;
print(int(num))

# print(int("123.4"))
print(int("123"))


print(float("123.4"))
print(int(float("123.4")))

num=30;
print(str(num))
print(type(str(num)))



print(bool(1))
print(bool(0))


print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))


print(bool("asd"))
print(bool("6"))
print(bool("6df"))
print(bool("@"))


name = "Python";
letter = list(name);

print(letter)



name = (1,2,34,5)
letter = list(name);

print(letter)


name = [1,2,3,4,5,76,76,3]

print(set(name))

data = [
    {"name","salman"},
    {"age",20},
    {"city","karachi"}
];

print(dict(data));


result = eval("10 + 20");

print(result)


print(chr(65))
print(chr(66))
print(chr(67))


print(chr(97))
print(chr(98))
print(chr(99))

print(chr(48))
print(chr(49))
print(chr(50))



print(chr(40))
print(chr(41))
print(chr(42))
print(chr(43))


for i in range(65,91):
    print(chr(i),end=" ")



print(ord("A"))
print(ord("B"))
print(ord("C"))


print(ord("👍"))


print(ord("a"))
print(ord("b"))
print(ord("c"))


print(ord("#"))
print(ord("*"))
print(ord("&"))


print(complex(5))
print(complex(5,7))