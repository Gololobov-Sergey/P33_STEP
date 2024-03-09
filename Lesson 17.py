
import random

def MinToMax(a, b):
    return a > b

def MaxToMin(a, b):
    return a < b

def evenFirst(a, b):
    if a % 2 == 1 and b % 2 == 0:
        return True
    if a % 2 == 0 and b % 2 == 1:
        return False
    return MinToMax(a, b)


def fromLastNumber(a, b):
    if a % 10 > b % 10:
        return True
    if a % 10 < b % 10:
        return False
    return MinToMax(a, b)


def bubbleSort(_list, method=MinToMax):
    for i in range(len(_list) - 1):
        for j in range(len(_list) - 1 - i):
            if method(_list[j], _list[j + 1]):
                _list[j], _list[j+1] = _list[j+1], _list[j]


n = int(input("n = "))
list1 = [random.randint(0, 1000) for i in range(n)]
print(list1)

bubbleSort(list1, fromLastNumber)

print(list1)

def hello():
    print("Hello")

def goodbye():
    print("Goodbye")

message = hello
message()
message = goodbye
message()

listFunc = [hello, goodbye]
for func in listFunc:
    func()

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def division(a, b):
    return a / b

def mod(a, b):
    return a % b

def power(a, b):
    return a**b

listOper = [plus, minus, mult, division, mod, power]
oper = ['+', '-', '*', '/', '%', '^']

expr = input()
for op1 in oper:
    if op1 in expr:
        var = expr.split(op1)
        print(f"{int(var[0])} {op1} {int(var[1])} = {listOper[oper.index(op1)](int(var[0]), int(var[1]))}")
else:
    print("Not operation!")







