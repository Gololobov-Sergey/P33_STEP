# 1 1 2 3 5 8 13 21 34 55 89 ....
'''f1 = 1
f2 = 1
# Fn = F(n-2) + F(n-1)
n = int(input("n = "))
k = 2
while k < n:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    k += 1
print(fn)'''

# Дано целое число N (> 0). Если оно является степенью числа 3, то вы-
# вести True, если не является — вывести False.

'''n = int(input("n = "))
k = 1
p = 0
while k < n:
    k *= 3
    p += 1
if k == n:
    print(p)
else:
    print(False)'''


# Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км.
# Каждый следующий день он увеличивал длину пробега на P процентов от
# пробега предыдущего дня (0 - 100). По данному P
# определить, после какого дня суммарный пробег лыжника за все дни пре-
# высит 200 км, и вывести найденное количество дней K (целое) и суммар-
# ный пробег S (вещественное число).

'''p = int(input("p = "))
run = 10
days = 1
result = 10
while result <= 200:
    days += 1
    per = run + run * (p/100)
    result += per
    run = per

print(f"{result} км на {days} день")'''


'''n = int(input("n = "))
s = 0
while n > 0:
    r = n % 10
    s += r
    n //= 10
print(s)'''



'''n = int(input("n = "))
s = 0
while n > 0:
    s += 1
    n //= 10
print(s)'''


'''n = int(input("n = "))
s = 0
while n > 0:
    r = n % 10
    if r % 2 == 1:
        s += r
    n //= 10
print(s)'''



# Даны положительные числа A, B, C. На прямоугольнике размера A × B
# размещено максимально возможное количество квадратов со стороной C
# (без наложений). Найти количество квадратов, размещенных на прямо-
# угольнике. Операции умножения и деления не использовать.

while -5:
    print("werwe")