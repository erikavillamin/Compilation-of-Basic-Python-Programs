#Ascending order
numbers = []
while True:
    try:
        num = int(input("Enter number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid")
        numbers.sort()
        print("The ascending order of numbers:", numbers)
        break
