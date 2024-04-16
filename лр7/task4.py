number = int(input("Введие число: "))
number2 = 0
for i in range(2, number // 2+1):
    if (number % i == 0):
        number2 = number2 + 1
if (number2 <= 0):
    print("Число простое")
else:
    print("Число не простое")