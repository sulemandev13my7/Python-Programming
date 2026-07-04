A  = {1,2,3};
B = {3,4,5};

print(A|B);

print(A.union(B));

print(A&B);

print(A.intersection(B));

print(A-B);

print(A.difference(B));

print(A ^ B);

print(A.symmetric_difference(B));


print(A.isdisjoint(B));

A  = {1,2,3,4};
B = {1,2,3,4,5,6};

print(A.issubset(B));

A  = {1,2,3,4,5,6,7};
B = {1,2,3,4,5,6};

print(A.issuperset(B));

x = len(A);
print(x);

number = [1,23,34,45,65,76,23];

unique_number = set(number);

print(unique_number)

fruits = {"orange","Apple"};

print(max(fruits))
print(min(fruits))