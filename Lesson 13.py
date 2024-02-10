import random
import string

'''n = int(input("n = "))
list1 = [random.randint(0, 10) for i in range(n)]
print(list1)'''

'''for i in range(len(list1) - 1):
    for j in range(len(list1) - 1 - i):
        if list1[j] < list1[j + 1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]'''

'''list1.sort(reverse=True)
print(list1)'''

'''st = 'mama Mama mama'
str1 = list(st)
print(str1)
print(st[1])
print(st.index('am'))
print(st.count("a"))
#st = st.replace('a', 'o')
#print(st)
print(st.find('amr'))
print(st.rfind('a'))
print(st.capitalize())
print(st.title())
print(st.upper())
print(st.lower())
print(st.split('ma'))
print(st.isalpha())
print("1".isdigit())
print("1234".isupper())
print("1234".islower())
print(st.isalnum())
print(st.isascii())
print("\t   \n".isspace())
print("Mama Mama".istitle())

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)

print(st[-1])'''

'''st = "Serhiy Gololobov"
s = st.split()
st1 = s[1] + " " + s[0]
print(st1)'''


st = "This image is a derivative work of the is following images"

'''st1 = st.split()
print(st1)
l = len(st1[0])
for s in st1:
    if len(s) > l:
        l = len(s)
        w = s
print(w)'''


# Дан символ C и строка S. Удвоить каждое вхождение символа C
# в строку S.
# mama m
# mmamma
'''c = input("sym : ")
print(st.replace(c, c*2))'''


# Даны строки S и S0. Удалить из строки S последнюю подстроку, сов-
# падающую с S0. Если совпадающих подстрок нет, то вывести строку S без
# изменений.

'''s0 = input("Sub str : ")
i = st.find(s0)
s2 = st[0:i] + st[i+len(s0):]
print(s2)'''


# Дана строка, содержащая по крайней мере один символ пробела. Вы-
# вести подстроку, расположенную между первым и вторым пробелом ис-
# ходной строки. Если строка содержит только один пробел, то вывести пус-
# тую строку.

#fgdsf 34534 ertrt erwer 345345
# 34534

s = st.split()
if len(s) < 3:
    print("pusto")
else:
    print(s[1])

