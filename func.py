def printLine(count=20, symbol='*'):
    for i in range(count):
        print(symbol, end='')
    print()

def countNumber(n):
    s = 0
    if n <= 0:
        s = 1
        n = abs(n)
    while n > 0:
        s += 1
        n //= 10
    return s

def countNumberList(_list):
    s = 0
    for i in _list:
        s += countNumber(i)
    return s


def printList(_list):
    l = countNumberList(_list) + len(_list)-1
    printLine(l, '*')
    for i in _list:
        print(i, end=' ')
    print()
    printLine(l, '*')