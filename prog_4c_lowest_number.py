#Display lowest number

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid")
        break
if numbers:
    print("The lowest number is", min(numbers), end=".")
else:
    print("Try again")
