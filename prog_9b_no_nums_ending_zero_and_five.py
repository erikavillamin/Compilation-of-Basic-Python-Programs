#Numbers from 0 to 100 with no ending zero and five
for num in range(101):
    if num % 10 not in [0,5]:
        print(num, end = ",")