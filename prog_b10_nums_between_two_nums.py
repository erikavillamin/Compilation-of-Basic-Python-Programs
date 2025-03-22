#All the numbers between the 2 numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: ")) 

if num1 < num2:
    for num in range(num1 + 1, num2):
        print(num, end=",")  
elif num1 > num2:
    for num in range(num1 - 1, num2, -1):
        print(num, end=",")
else:
    print("No numbers between same inputs.")
