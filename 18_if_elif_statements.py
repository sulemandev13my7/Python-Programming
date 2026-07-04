per = float(input('Enter your score : '))

if per >= 80 and per <= 100:
    print("MERIT");
elif per >= 70 and per < 80:
    print("Frist");
elif per >= 60 and per < 70:
    print("Second");
elif per >= 50 and per < 60:
    print("Third");
elif per >= 35 and per < 50:
    print("Passed");
else:
    print("Invalid Number")

    
age = 20;

if age >=18:
    print('Adult');
elif age < 18:
    print('Child');
else :
    print('You are not eligible')

username = input('Enter Your name : ')
password = int(input('Enter Your password : '))

if username != "admin":
    print('Invalid Username');
elif password != 1234:
    print('Invalid Password');
else:
    print('Login Successfull')