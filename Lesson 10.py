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

c = 0
for h in range(24):
    for m in range(60):
        h1 = h // 10
        h2 = h % 10
        m1 = m // 10
        m2 = m % 10
        if h1 == m2 and h2 == m1:
            print(f"{h1}{h2}:{m1}{m2}")
            c += 1
print(c)