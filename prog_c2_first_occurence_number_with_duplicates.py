#Showing only the first entry for duplicates

numbers = [float(input(f"Enter number {num + 1}: ")) for num in range(10)]
duplicates = set()
first_dup = [num for num in numbers if not (num in duplicates or duplicates.add(num))]

print("The first entry number/s in duplicates:", first_dup)

