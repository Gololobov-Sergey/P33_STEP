'''a = int(input("a = "))
b = int(input("b = "))

for i in range(a, b+1):
    f = True
    for j in range(2, i):
        if i % j == 0:
            f = False
            break
    if f:
        print(i, end=' ')'''


'''n = int(input("n = "))
for k in range(3):
    for i in range(k+3):
        for j in range(n-i-1+3-k):
            print(' ', end='')
        for j in range(2*i+1+2*k):
            print('*', end='')
        print()'''