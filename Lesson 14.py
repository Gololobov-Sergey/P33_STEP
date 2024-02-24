import random
import func

'''n = int(input("n = "))
list1 = [random.randint(-1000, 1000) for i in range(n)]
print(list1)'''



'''c = int(input("c = "))
printLine(symbol='#', count=c)
print(list1)
printLine(30, '*')'''

def summa(a, b, c=0, d=0):
    c = a + b + c + d
    return c

'''print(summa(1,2))
print(summa(1,2, 3))
print(summa(1,2, 3, 4))'''

'''a = int(input("a = "))
b = int(input("b = "))
print(summa(a, b))
print(printLine(30, '*'))'''

#a = int(input("a = "))
#a = int(input())

def isEven(num):
    return num % 2 == 0

'''c = 0
for i in list1:
    if isEven(i):
        c += 1'''

#print(c)

#a = int(input())

def krt3(num):
    return num % 3 == 0

def isPositive(num):
    return num > 0

def isNegative(num):
    return num < 0

#print(krt3(10) and isPositive(10))
#print(krt3(10) and isNegative(10))



#func.printList(list1)

func.printLine(20, '#')
func.printLine(30)
func.printLine()

#  *******************
#  6 8 5 3 1 7 0 6 0 2
#  *******************

count = 5
def foo():
    global count
    count += 10


print(count)
foo()
print(count)

def foo1(a, *args):
    for i in args:
        print(i, end=' ')

def foo2(**kwargs):
    for k in kwargs:
        print(k, kwargs[k])

foo1(1,2,4,7,9,8,6,4,3,3,5,67,8,9,0)
foo2(k=1, b=2, ff=255)

def luckyNumber(a):
    a1 = a % 10
    a2 = a // 10 % 10
    a3 = a // 100 % 10
    a4 = a // 1000 % 10
    a5 = a // 10000 % 10
    a6 = a // 100000
    return a1 + a2 + a3 == a4 + a5 + a6

print(luckyNumber(123122))
print(luckyNumber(123122))
print(luckyNumber(123122))
print(luckyNumber(123122))
# 000001 - 999999