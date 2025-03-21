#Display the highest number
numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid")
        break
        
if numbers:
    print("The highest number is", max(numbers), end=".")
else:
    print("Try again")


