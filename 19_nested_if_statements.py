age = 18;
citizen = True;

if age >=18:
    if citizen == True:
        print('Eligible to vote. ');
    else:
        print('Must be a Citizen to vote. ')
else:
    print("Must be at least 18 years old to vote. ");
    


balance = 15000;
withdraw = 5000;

if balance >= withdraw:
    if withdraw <= 10000:
        print('Transection Successfull')
    else:
        print('withdraw limit exceeded. Maximum allowed is 10,000');
else:
    print("You don't have sufficent balance")

age = int(input('Enter Your age .. '));
has_license = input('DO You have a license ? (yes/no) ');

if age >= 18:
    if has_license == "yes":
        print('You can Drive');
    else:
        print('You need to driving license')
else:
    print('Your are under age');