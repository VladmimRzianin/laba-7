number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")
number3 = input("Введите третье число: ")
if number1 > number2 and number1 > number3:
    print(number1)
if number2 > number1 and number2 > number3:
    print(number2)
if number3 > number2 and number3 > number1:
    print(number3)