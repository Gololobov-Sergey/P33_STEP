'''a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
s = 0
for i in range(3):
    if a > 0:
        s += 1
    if b > 0:
        s += 1'''

'''s = 0
l = [1,2,-3,3,54,7,89,-6,4,3,2]
print(l[1])
for i in l:
    if i > 0:
        s += 1
print(s)

list1 = [1, "mama", 4.88, True]
for i in list1:
    print(i)'''

'''s = 0
s1 = 0
list2 = [0,0,0,1,1,1,0,0,1,0,1]
for i in range(len(list2)):
    if list2[i] == 0:
        s += 1

for i in list2:
    if i == 0:
        s1 += 1
    else:
        break

print(s)
print(s1)'''

import random
n = int(input("n = "))
'''list3 = []
for i in range(n):
    list3.append(random.randint(-10, 10))
print(list3)'''
list3 = [random.randint(-10, 10) for i in range(n)]
#list3 = [i*2 for i in range(n)]

'''s = 0
a = int(input("a = "))
for l in list3:
    if l == a:
        s += 1
print(s)'''

'''s = 0
for i in range(len(list3)):
    if list3[i] < 0 and i % 2 == 1:
        s += 1
print(s)'''

'''maxValue = list3[0]
for elem in list3:
    if elem > maxValue:
        maxValue = elem
print(max)'''

#print(max(list3))
#print(min(list3))


'''imax = 0
maxValue = list3[imax]
for i in range(len(list3)):
    if list3[i] > maxValue:
        maxValue = list3[i]
        imax = i
print(maxValue)
print(imax)'''

#print(list3.index(max(list3)))

imax = list3.index(max(list3))
imin = list3.index(min(list3))
print(imax)
print(imin)

s = 0
if imax > imin:
    start, end = imin, imax
else:
    start, end = imax, imin

for i in range(start+1, end):
    s += list3[i]
print(s)

imax = 0
maxValue = list3[imax]
imin = 0
minValue = list3[imax]
for i in range(len(list3)):
    if list3[i] > maxValue:
        maxValue = list3[i]
        imax = i
    if list3[i] < minValue:
        minValue = list3[i]
        imin = i
print(maxValue)
print(imax)