a = 10;
b = 6;

print(a & b) # 10 = 1010, 6 = 0110, 1010 & 0110 = 0010 = 2
print(bin(a)) # 01010
print(bin(b)) # 0110
print(bin(a & b)) # 0010
print(bin(a | b)) # 1110
print(bin(a ^ b)) # 1100
print(bin(~a)) # -0b1011
print(~a) # -11  ~x = -(x+1)  ~10 = -(10+1) = -11
# use of bitwise operator in python in operating type softwere or network coding 

# <<left shift operator multiply by 2
x = 10; # 1010
print(x << 1) # 10100 = 20 
print(x << 2) # 101000 = 40
print(bin(x << 1)) # 0b10100
print(bin(x << 2)) # 0b101000

# >>right shift operator divide by 2
x = 10; # 1010
print(x >> 1) # 0101 = 5
print(x >> 2) # 0010 = 2
print(bin(x >> 1)) # 0b101
print(bin(x >> 2)) # 0b10