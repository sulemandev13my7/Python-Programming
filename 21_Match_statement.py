 day = int(input('Enter Your day..'))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("Weekend")
    case _:
        print('Enter the correct week day')



A = float(input('Enter value A.. '))
B = float(input('Enter value B.. '))
operator = input('Enter Your operator.. ')

match operator:
    case "+":
        print("Addition : ", A + B)
    case "-":
        print("Subtraction : ", A - B  )
    case "*":
        print("Multiplication : ", A * B)
    case "/":
        print("Division : ", A / B)
    case _:
        print('Enter the correct operator')
        
        
        
month = input('Enter Your month..  ')

match month:
    case "December" | "January" | "February":
        print("Winter")
    case "March" | "April" | "May":
        print("Spring")
    case "June" | "July" | "August":
        print("Summer")
    case "September" | "October" | "November":
        print("Autumn")
    case _:
        print('Enter the correct month')


data = [10,20];

match data:
    case [10,20]:
        print("Both number are same")
    case [10]:
        print('only one number are same')
    case _:
        print('unknown number')


        
point = (10,20);

match point:
    case (0,0):
        print("Origin")
    case (0,y):
        print('Y axis',y)
    case (x,0):
        print('X axis',x)
    case (x,y):
        print('Both are same',x,y)
    case _:
        print('unknown Point')
        

student = {
    'name' : 'John',
    'age' : 20
}

match student:
    case {'name': 'John', 'age': 20}:
        print("Student is John and is 20 years old")
    case {'name': 'John'}:
        print("Student is John")
    case _:
        print("Unknown student")
        

age = 20;
match age:
    case x if x < 18:
        print("Minor")
    case x if x < 65:
        print("Adult")
    case x if x >= 65:
        print("Senior citizen")
        
point = (20, 30);
match point:
    case (x, y) if x < 18 and y < 18:
        print("Both are minors")
    case (x, y) if x >= 18 and y >= 18:
        print("Both are adults")
    case _:
        print("Mixed ages")