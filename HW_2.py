# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11
n = input()
m = 0
x = len(n)-2
n = int(float(n) * 10 ** x)
print(n)
while n:
    m += n % 10
    n //=10
print(m)
#*** Variant 2


n = input().replace(',','').strip('-')
n_list = list(n)
n_num = map(int,n_list)
print(sum(n_num))
# *************
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input())
x = 1
for i in range(1, n+1):
    x = x * i
    print(x, end=' ')

# **************

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input())
x = {}
for i in range(1, n + 1):
    v = i * 3 + 1
    x[i] = v
print(x)


# ************************
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных #позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.




def list_x(n):
    list_1 = list(range(-n, n + 1))
    print(list_1)
    with open('file.txt', 'r') as data:
        x = int(data.readline().strip())
        m = int(data.readline().strip())
        if x <= len(list_1) and m <= len(list_1):
            return list_1[x - 1] * list_1[m - 1]
        return False


print(list_x(5))



# *************
# Реализуйте алгоритм перемешивания списка.
import random
def mixt_list(x):

    for i in range(len(x)):
        ind = random.randrange(len(x))
        x[i], x[ind] = x[ind],  x[i]
    return x

print(mixt_list(list(range(9))))
