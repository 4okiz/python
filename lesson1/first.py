# 1
a = input()
b = input()
c = input()

print(a)
print(b)
print(c)


# 2
t = int(input('Введи время в секундах\n'))

h = 0
m = 0
s = 0

if t >= 60:
    m = t // 60
    s = t % 60
    if m >= 60:
        h = m //60
        m = m % 60

print(f'{h}:{m}:{s}')


# 3
n = input()

print(f'Result:{n}+{n}{n}+{n}{n}{n} = {int(n) + int(n + n) + int(n + n + n)}')


# 4
n = int(input())
n_list = []
if len(str(n)) > 1:
    for _ in str(n):
        n_list.append(int(_))
else:
    print(n)
print(max(n_list))


# 5
profit = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Рентабельность выручки составила {profit / costs}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль сотавила {profit / workers}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")


# 6
a = 2
b = 3

count = 1

while a < b:
    print(f'{count} день: {a}')
    a = a + a/10
    count += 1
print(f'{count} день: {a} - в этот день спортсмен достиг отметки в {b} км')