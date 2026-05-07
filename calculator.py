first_number =int(input('Enter first number:'))
Operators = input("Enter operators (+,-,*,/,%):")
second_number =int(input('Enter second number:'))

if Operators == "+":
    print("Result:",first_number+second_number)
elif Operators == "-":
    print("Result:",first_number-second_number)
elif Operators == "*":
    print("Result:",first_number*second_number)
elif Operators == "/":
    print("Result:",first_number/second_number)
elif Operators == "%":
    print("Result:",first_number%second_number)
else:
    print("invalide Operation")