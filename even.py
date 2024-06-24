user_input = int(input("enter the number: "))
number = 0
for number in range(user_input + 1):
    if number % 2 == 0:
        print(number)
    else:
        continue
