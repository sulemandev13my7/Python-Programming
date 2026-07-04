# Numaric datatype

y = 20;
print(y)
print(type(y))#int

z = 23.56;
print(z)
print(type(z))#float

a = 2+3j;
print(a);
print(type(a))#complex

#Text datatype
x="Data";
print(x)
print(type(x))#str


# Sequence datatype
l = ["orange","mango","bananas"];
print(l);
print(type(l))#list

t = (12,"ertryt",45.67);
print(t)
print(type(t));#tuple

r = range(5);
print(r)
print(type(r))#range(0,5)
print(list(r))#[0, 1, 2, 3, 4]


#Mapping
d = {'name':"salman",'age':12,'height':5};
print(d)
print(type(d));#dict

# set
s = {'name','age',45};
print(s)
print(type(s));#set

x = frozenset({'name','age',45});
print(x)
print(type(x));#frozenset

# boolean
b = True;
print(b)
print(type(b));#bool

x = 13 > 10;
print(x);#true
x = None;
print(x)
print(type(x));#NoneType
 
x= b"hello";
print(x)
print(type(x));#bytes

x = bytearray([2,34,45,56]);
print(x)
print(type(x));#bytearray

m = memoryview(bytes(5));
print(m)
print(type(m));#memoryview


