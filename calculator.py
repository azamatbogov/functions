import math

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ValueError("Ошибка: Деление на ноль!")
    return num1 / num2

def exp(num1, num2):
    return num1 ** num2

def sq(num1):
    if num1 < 0:
        raise ValueError("Ошибка: Квадратный корень отрицательного числа!")
    return math.sqrt(num1)

def factorial(num1):
    if num1 < 0:
        raise ValueError("Ошибка: Факториал отрицательного числа!")
    result = 1
    for i in range(1, int(num1) + 1):
        result *= i
    return result

def sin(num1):
    return math.sin(num1)

def cos(num1):
    return math.cos(num1)

def tg(num1):
    return math.tan(num1)

print("Инженерный калькулятор")
while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")

    choice = input("Введите номер операции: ")

    if choice == "0":
        print("Выход из калькулятора.")
        break

    try:
        num1 = float(input("Введите первое число: "))
        if choice not in ("6", "7", "8", "9", "10"):
            num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите числа.")
        continue

    try:
        if choice == "1":
            result = addition(num1, num2)
        elif choice == "2":
            result = subtraction(num1, num2)
        elif choice == "3":
            result = multiplication(num1, num2)
        elif choice == "4":
            result = division(num1, num2)
        elif choice == "5":
            result = exp(num1, num2)
        elif choice == "6":
            result = sq(num1)
        elif choice == "7":
            result = factorial(num1)
        elif choice == "8":
            result = sin(num1)
        elif choice == "9":
            result = cos(num1)
        elif choice == "10":
            result = tg(num1)
        else:
            print("Неправильный выбор операции. Пожалуйста, выберите снова.")
            continue

        print(f"Результат: {result}")
    except ValueError as e:
        print(e)
