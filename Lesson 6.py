
'''M = int(input("Вага загальна - "))
Z1 = int(input("Вага зайця, кг - "))
Z2 = int(input("Вага зайця, гр - "))
Z = 1000*Z1 + Z2
K = 1000*M - Z
#...
print(K)
print(Z)'''


# Дано целое число. Вывести его строку-описание вида «отрицательное чет-
# ное число», «нулевое число», «положительное нечетное число» и т. д.

'''n = int(input("n = "))
if n == 0:
    print("нульове число")
else:
    if n > 0:
        print("додатне", end=' ')
    else:
        print("відємне", end=' ')

    if n % 2 == 0:
        print("парне число")
    else:
        print("непарне число")'''


'''p = int(input("P l = "))
if p >= 0:
    m = int(input("m % = "))
    if m >= 0 and m <= 100:
        k1 = p*10*m  # ml p*1000 * m / 100
        k2 = int(input("K2 ml = "))
        if k2 >= 0 and k2 <= 1000*p - k1:
            k3 = 1000*p - k1 - k2
            if k1 > k3:
                print("k1 > k3")
            elif k1 < k3:
                print("k1 < k3")
            else:
                print("k1 = k3")
        else:
            print("Error data")
    else:
        print("Error data")
else:
    print("Error data")'''


'''
n = int(input('n = '))
k = int(input('k = '))
m = int(input('m = '))
if k+m == n+1:
    print('Кімнати знаходяться навпроти')
else:
    print('Кімнати не знаходяться навпроти')'''


direction = input("Dir - (w, s, n, e)")
com1 = int(input("Command 1 - "))
com2 = int(input("Command 2 - "))

pos = 0
if direction == 'n':
    pos = 0
elif direction == 'e':
    pos = 1
elif direction == 's':
    pos = 2
else:
    pos = 3

pos += com1
pos += com2

pos %= 4

if pos == 0:
    direction = 'n'
elif pos == 1:
    direction = 'e'
elif pos == 2:
    direction = 's'
else:
    direction = 'w'

print(direction)