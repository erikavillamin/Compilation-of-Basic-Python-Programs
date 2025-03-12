# Total of even numbers in 10 numbers
even_num = 0

for even in range(10):
    num = int(input(f"Enter number {even + 1}: "))
    if num % 2 == 0:
        even_num +=1
        
print(f"The total even numbers is: {even_num}")
