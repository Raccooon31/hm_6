rad = input("Введіть вираз наприклад, 23+12: ")

num1, operator, num2 = rad.split()
num1, num2 = float(num1), float(num2)

if operator == '+':
        result = num1 + num2
elif operator == '-':
        result = num1 - num2
elif operator == '*':
        result = num1 * num2
elif operator == '/':
    if num2 == 0:
            print("Помилка: ділення на 0")
    result = num1 / num2

print(f"Результат виразу {rad} дорівнює {result}")

