#Quotient without decimal points
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 != 0: 
    quotient = int(num1 // num2)
    print(f"The quotient of the two numbers is: {quotient}")
else:
    print("Invalid input. Enter new number.") #Division by zero not allowed
