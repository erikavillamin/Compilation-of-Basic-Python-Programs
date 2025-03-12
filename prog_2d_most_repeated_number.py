from collections import Counter

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break 

if numbers:
    counts = Counter(numbers)

    
    max_count = max(counts.values())

    
    most_repeated = [num for num, count in counts.items() if count == max_count]

    
    if len(most_repeated) == 1:
        print(f"The most repeated number is: {most_repeated[0]}")
    elif max_count == 1:
        print("No numbers have duplicate.")
    else:
        print(f"The numbers {most_repeated} have the same number of duplicates.")
        
else:
    print("Invalid")

