#Descending order
numbers = []
while True:
    try:
        num = int(input("Enter number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid")
        numbers.sort(reverse=True)
        print("The descending order of numbers:", numbers)
        break
