#Display lowest number

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid")
        break
print("The lowest number is", min(numbers), end=".")
