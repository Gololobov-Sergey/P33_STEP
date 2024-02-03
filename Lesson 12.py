import random
'''n = int(input("n = "))
list1 = [random.randint(0, 10) for i in range(n+3)]
list2 = [random.randint(0, 10) for i in range(n-2)]
print(list1)
print(list2)

list3 = []
for i in list1:
    if i in list2 and i not in list3:
        list3.append(i)

print(list3)'''



# Дано число R и массив A размера N. Найти элемент массива, который
# наиболее близок к числу R

'''n = int(input("n = "))
r = int(input("r = "))
list1 = [random.randint(0, 100) for i in range(n)]
print(list1)

minR = r - min(list1)
value = 0
for i in list1:
    if abs(i - r) < minR:
        minR = abs(i - r)
        value = i
print(value)'''

'''import math
R = int(input("R = "))
r = int(input("r = "))
h = int(input("h = "))
d = 0
for x in range(-R, R, h):
    for y in range(-R, R, h):
        if r < math.sqrt(x**2 + y**2) < R:
            d += 1
print(d)'''


n = int(input("n = "))
list1 = [[random.randint(0, 10) for i in range(n)] for j in range(n)]
#print(list1[1][2])
for i in range(len(list1)):
    sumRow = 0
    for j in range(len(list1[0])):
        sumRow += list1[i][j]
        print(f"{list1[i][j]:3}", end=' ')
    print(" | ", sumRow)

'''print()
maxVal = list1[0][0]
for l in list1:
    for elem in l:
        if elem > maxVal:
            maxVal = elem;
        print(f"{elem:3}", end=' ')
    print()

print(maxVal)'''