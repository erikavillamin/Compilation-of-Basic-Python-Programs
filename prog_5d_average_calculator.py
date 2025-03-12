# Average Calculator
numbers = []

while True:
    try:
        num = float(input("Enter a number: "))  
        numbers.append(num)
    except ValueError:
        print("Invalid")
        break

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average of all numbers is: {average:.2f}") 
else:
    print("Try again")

