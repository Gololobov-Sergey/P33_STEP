# Даны координаты поля шахматной доски x, y (целые числа, лежа-
# щие в диапазоне 1–8). Учитывая, что левое нижнее поле доски (1, 1) явля-
# ется черным, проверить истинность высказывания: «Данное поле является
# белым».

'''x = int(input("x = "))
y = int(input("y = "))
if (x + y) % 2 == 1:
    print("white")
else:
    print("black")'''

# Даны координаты двух различных полей шахматной доски x1, y1,
# x2, y2 (целые числа, лежащие в диапазоне 1–8). Проверить истинность вы-
# сказывания: «Данные поля имеют одинаковый цвет».

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print(True)
else:
    print(False)

# Даны координаты двух различных полей шахматной доски x1, y1,
# x2, y2 (целые числа, лежащие в диапазоне 1–8). Проверить истинность вы-
# сказывания: «Ладья за один ход может перейти с одного поля на другое».