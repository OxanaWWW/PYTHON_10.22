# Вычислить число c заданной точностью d

# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#
from math import pi

_, x = input().split('.')
print(round(pi, len(x)))

# ****2 variant*****

a = input().split('.')
print(round(pi, len(a[1])))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.



n = int(input())
i = 2
m = []

while n > 1:
    if n % i == 0:
        m.append(i)
        n /= i

    else:
        i += 1
print(m)

# ****************
# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
list_1 = list(map(int,input().split()))
list_2 = [i for i  in list_1 if list_1.count(i) == 1]
print(list_2)


# ******************
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random


def write_f(k):
    x = ''
    with open('5.txt', 'a') as data:
        for i in range(k, 1, -1):
            a = random.randint(0, 101)
            if a:
                x += f'{a}* x^{i} {random.choice("+-")} '
        data.writelines([x, str(random.randint(0, 101)), '* x', ' ', random.choice("+-"), ' ',
                         str(random.randint(0, 101)), ' = 0\n'])


write_f(int(input()))



# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def write_f():
    x = ''
    with open('5.txt','r') as data_1, open('6.txt','r') as data_2, open('sum.txt','a') as data_3:
        a = data_1.readline()
        b = data_2.readline()
        data_3.write(f'{a[:-5]} + {b}')


write_f()

import random

def write_f(k):
    x = ''
    with open('6.txt','a') as data:
        for i in range(k,1,-1):
            a = random.randint(0,101)
            if a:
                x += f'{a}* x^{i} {random.choice("+-")} '
        data.writelines([x, str(random.randint(0,101)), '* x',' ',random.choice("+-"),' ',
                         str(random.randint(0,101)),' = 0\n'])
