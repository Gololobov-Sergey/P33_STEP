'''f = open("text.txt", 'w', encoding="utf-8")
f.write("Слава Україні!")
f.close()'''

import random
'''n = int(input("n = "))
list1 = [random.randint(0, 10) for i in range(n)]
print(list1)

f = open("list.txt", 'w')
for i in list1:
    f.write(str(i) + " ")
f.close()'''


'''f = open("list.txt", 'r')
list2 = [int(i) for i in f.readline().split()]
print(list2)

f = open("Lesson 18.py", 'r')
st = f.readlines()
for s in st:
    print(s, end='')'''

# Дано имя файла и целое число N (0 < N < 27). Создать текстовый файл с
# указанным именем и записать в него N строк: первая строка должна со-
# держать строчную (то есть маленькую) латинскую букву «a», вторая —
# буквы «ab», третья — буквы «abc» и т. д.; последняя строка должна содер-
# жать N начальных строчных латинских букв в алфавитном порядке.

import string

print(string.ascii_lowercase)


'''f = open("log.txt", 'w')
week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
for i in range(10000):
    f.write("192.168.0." + str(random.randint(100, 255)) + " " + random.choice(week) + ' ' +
            str(random.randint(0, 23)).zfill(2) + ':' + str(random.randint(0, 59)).zfill(2) + ' ' +
            str(random.randint(0, 23)).zfill(2) + ':' + str(random.randint(0, 59)).zfill(2) + '\n')'''

'''n = 15
f = open("abc.txt", 'w')
for i in range(n):
    f.write(string.ascii_lowercase[:i+1] + '\n')'''

f = open('log.txt', 'r')
ip = f.readlines()
logs = []
for st in ip:
    logs.append(st.split())
#print(logs)

ip_uniqe = []
for row in logs:
    if row[0] not in ip_uniqe:
        ip_uniqe.append(row[0])


all_ip = [i[0] for i in logs]
count_ip = []
for ip in ip_uniqe:
    count_ip.append(all_ip.count(ip))

maxCount = max(count_ip)
i = count_ip.index(maxCount)
print(ip_uniqe[i])
print(maxCount)

import datetime

'''t = datetime.datetime(2024, 3, 16)
t1 = datetime.datetime.now()
print(t1)
t2 = t1 - t
print(t2)'''



list_time = []
for row in logs:
    t1 = row[2].split(':')
    t2 = row[3].split(':')
    tt1 = datetime.time(hour=int(t1[0]), minute=int(t1[1]))
    tt2 = datetime.time(hour=int(t2[0]), minute=int(t2[1]))
    if tt2 < tt1:
        t = datetime.datetime(2024, 1, 2, hour=int(t2[0]), minute=int(t2[1])) - datetime.datetime(2024, 1, 1, hour=int(t1[0]), minute=int(t1[1]))
    else:
        t = datetime.datetime(2024, 1, 1, hour=int(t2[0]), minute=int(t2[1])) - datetime.datetime(2024, 1, 1, hour=int(t1[0]), minute=int(t1[1]))
    list_time.append(t.seconds)
print(list_time)