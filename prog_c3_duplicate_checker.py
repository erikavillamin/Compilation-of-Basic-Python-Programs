#Checking duplicates

numbers = []
while True:
    try:
        num = int(input("Enter number: "))
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.append(num)
    except ValueError:
        print("Invalid")
        break
