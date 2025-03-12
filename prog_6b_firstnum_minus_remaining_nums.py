#First number minus the remaining numbers
numbers = [float(input(f"Enter number {num +1}: ")) for num in range(10)]
difference = numbers[0] - sum(numbers[1:])
print(f"The result is: {difference}")