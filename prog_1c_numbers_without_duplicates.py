#Input 10 numbers and display all numbers that don't have duplicate

numbers = [float(input(f"Enter number {num + 1}: ")) for num in range(10)]
unique_num = [num for num in numbers if numbers.count(num) == 1]

print("Answer: ", unique_num)

