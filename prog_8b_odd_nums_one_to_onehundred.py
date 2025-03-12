#Odd numbers from 0 to 100 (while loop)
num = 0
while num <= 100:
    if num % 2 != 0:
        print(num, end = ",")
    num += 1