# f = open("students.txt","w");

# w = f.write("Hello Python")
# f.close()

# w = f.write("Hello Python\n")
# w = f.write("Suleman\n")
# w = f.write("Usman \n")
# f.close()

# print(w)




# names = [
#     "salman\n",
#     "ayan\n",
#     "salo\n",
# ]

# w = f.writelines(names)

# f.close()



# f = open("students.txt","a");

# f.write("salman khan")

# f.close()




# f = open("students.txt","r+");

# print(f.read())

# f.write("\nPython")

# f.close()





# f = open("students.txt","w+");

# f.write("\nBahi sahab")

# f.seek(0)

# print(f.read())

# f.close()




# f = open("students.txt","a+");

# f.write("\nBahi")

# f.seek(0)

# print(f.read())

# f.close()



# f = open("students1.txt","x");

# f.write("Python")

# f.close()



# import os

# os.remove("students1.txt")



import os

if os.path.exists("students1.txt"):
    os.remove("students1.txt")
    print("File deleted")
else:
    print("File not found")