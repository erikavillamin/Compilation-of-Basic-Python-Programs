#Display the numbers that have duplicates
numbers = [float(input(f"Enter number {num + 1}: ")) for num in range(10)]
duplicates = list(set([num for num in numbers if numbers.count(num) > 1]))

if duplicates:
    print("The number(s) that have duplicates:", duplicates)
else:
    print("No number with duplicates")


