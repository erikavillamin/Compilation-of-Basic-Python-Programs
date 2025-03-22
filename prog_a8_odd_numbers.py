# Total of odd numbers in 10 numbers
odd_num = 0

for odd in range(10):
    num = int(input(f"Enter number {odd + 1}: "))
    if num % 2 != 0:
        odd_num +=1
        
print(f"The total odd numbers is: {odd_num}")
