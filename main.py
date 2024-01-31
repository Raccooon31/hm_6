#Завдання 1
# rad = input("Введіть рядок на перевірку чи є він паліндромом: ")
#
# rad2 = rad.replace(" ", "").lower()
# print(rad2)
#
# rad3 = rad2[::-1]
#
# if rad2 == rad3:
#     print("Ваш ряд паліндром")
# else:
#     print("Ваш ряд не паліндром")

#Завдання 2
#Не зрозумів завдання

#Завдання 3
simvl1 = "."
simvl2 = "!"
simvl3 = "?"
rad = input("Введіть рядок: ")
tret = rad.count(simvl3)
vtor = rad.count(simvl2)
perv = rad.count(simvl1)
col_rech = tret+vtor+perv
print(f"Кількість речень в вашому рядку така: {col_rech}")