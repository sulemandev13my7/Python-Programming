age = 16;

if age >= 18:
    status = "Adult";
else:
    status = "Minor";
    
print(status)

age = 18;
status = "Adult" if age >= 18 else "Minor"
print(status)


num = 124;
status = "Even" if num %2 == 0 else "Odd"
print(status)

marks = 82;
result = "Grade A" if marks >= 90 else "B"
print('Result :', result)


marks = 37;
result = "Grade A" if marks >= 90 else "B" if marks >= 80 else "C"
print('Result :', result)


marks = 37;
result = (
    "Grade A" if marks >= 90 else
    "B" if marks >= 80 else
    "C" if marks >= 60 else
    "D" if marks >= 45 else
    "Fail"
    )
print('Result :', result)


marks = 97;
result = (
    "1st division" if marks >= 90 else
    "2nd division" if marks >= 80 else
    "3rd division" if marks >= 70 else
    "4th division" if marks >=60 else
    "Fail"
)
print(result)