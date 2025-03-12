#Numbers from 0 to 100 without ending zero
for num in range(101):
    if num % 10 != 0:
        print(num, end=",")
    