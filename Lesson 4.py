'''print(5 > 5)
print(5 < 3)
print(5 == 5)
print(5 >= 5)
print(5 <= 5)
print(5 != 4)

a = 5
b = not (5 < 5)
print(b)

print("-----------")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(5 > 5 or 5 == 5)

print("-----------")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(5 > 5 and 5 == 5)'''

# Дано целое число A. Проверить истинность высказывания: «Число
# A является положительным».

'''a = int(input("a = "))
r = a > 0
print(r)'''

#=================================================================

# Дано целое число A. Проверить истинность высказывания: «Число A
# является нечетным».

'''a = int(input("a = "))
r = a % 2 == 1
print(r)'''

#=================================================================

# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A > 2 и B ≤ 3».

'''a = int(input("a = "))
b = int(input("b = "))
r = a > 2 and b <= 3
print(r)'''

#=================================================================

# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Справедливо двойное неравенство A < B < C».

'''a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
r = a < b and b < c
print(r)'''

#=================================================================

# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Число B находится между числами A и C».

'''a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
r = a < b and b < c or c < b and b < a
print(r)'''

#=================================================================

# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Каждое из чисел A и B нечетное».

'''a = int(input("a = "))
b = int(input("b = "))
r = a % 2 == 1 and b % 2 == 1
print(r)'''

#=================================================================

# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Числа A и B имеют одинаковую четность».

'''a = int(input("a = "))
b = int(input("b = "))
r = a % 2 == b % 2
print(r)'''

#=================================================================

# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Каждое из чисел A, B, C положительное».

'''a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
r = a > 0 and b > 0 and c > 0
print(r)'''

#=================================================================

# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Ровно одно из чисел A, B, C положительное».

'''a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
#r = a > 0 and b < 0 and c < 0 or \
#    b > 0 and a < 0 and c < 0 or \
#    c > 0 and a < 0 and b < 0
r = int(a > 0) + int(b > 0) + int(c > 0) == 1
print(r)'''


# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Ровно два из чисел A, B, C являются положительными».


# Дано целое положительное число. Проверить истинность высказы-
# вания: «Данное число является четным двузначным».

a = int(input("a = "))
r = a % 2 == 0 and a > 9 and a < 100
print(r)

# Дано целое положительное число. Проверить истинность высказы-
# вания: «Данное число является нечетным трехзначным».
#r = a % 2 == 1 and a > 99 and a < 1000

# Проверить истинность высказывания: «Среди трех данных целых
# чисел есть хотя бы одна пара совпадающих».

'''a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
r = a == b or a == c or b == c
print(r)'''

# Проверить истинность высказывания: «Среди трех данных целых
# чисел есть хотя бы одна пара взаимно противоположных».

'''a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
r = a == -b or a == -c or b == -c
print(r)'''

# Дано трехзначное число. Проверить истинность высказывания:
# «Все цифры данного числа различны».
