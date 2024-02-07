#Завдання 1
# rad = input("Введіть вираз: ")
#
# znaki = ['+', '-', '*', '/']
#
# for i in znaki:
#     if i in rad:
#         index_znaka = rad.find(i)
#         break
#
# num1 = float(rad[:index_znaka])
# znak = rad[index_znaka]
# num2 = float(rad[index_znaka+1:])
#
# if znak == '+':
#     res = num1 + num2
# elif znak == '-':
#     res = num1 - num2
# elif znak == '*':
#     res = num1 * num2
# elif znak == '/':
#     if num2 != 0:
#         res = num1 / num2
#     else:
#         print("Ділити на 0 неможливо")
#         exit()

# print(f"Результат виразу {rad} = {res}")

#Завдання 2
from random import randint

lst = []
for i in range(10):
    lst.append(randint(-50, 50))

print(lst)

min_elem, max_elem = 0, 0

neg_count, pos_count, zero_count = 0, 0, 0

for num in lst:
    if num > max_elem:
        max_elem = num
    if num < min_elem:
        min_elem = num

    if num < 0:
        neg_count += 1
    elif num > 0:
        pos_count += 1
    else:
        zero_count += 1

print(f"Максимальне число = {max_elem}")
print(f"Мінімальне число = {min_elem}")
print(f"Кількість від'ємних чисел = {neg_count}")
print(f"Кількість додатніх чисел = {pos_count}")
print(f"Кількість нулів = {zero_count}")