#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#first variant:
# n = int(input())
# x = 1
# for i in range(1, n+1):
#     x = x * i
#     print(x, end=' ')
#second variant:
x = 1
[print(x := x * i, end=' ') for i in range(1, int(input()) + 1)]

# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#first variant:

# def RLE_decod(x):
#     a = ''
#     count = 1
#     for i in range(len(x) - 1):
#         if x[i] == x[i + 1]:
#             count += 1
#         else:
#             a += f'{count}{x[i]}'
#             count = 1
#     return a

#second variant:
from itertools import groupby


def RLE_decod(x):
    return ''.join([f'{len(list(word))}{y}' for y, word in groupby(x)])


print(RLE_decod(input()))


#Найти произведение пар чисел в списке. ... Написать программу вычисления арифметического выражения,
# заданного строкой. Используются операции +,-,/,. приоритет операций стандартный.
# Пример: 2+2 => 4; 1+23 => 7; 1-23 => -6


actions = {
        "^": lambda x, y: str(float(x) ** float(y)),
        "*": lambda x, y: str(float(x) * float(y)),
        "/": lambda x, y: str(float(x) / float(y)),
        "+": lambda x, y: str(float(x) + float(y)),
        "-": lambda x, y: str(float(x) - float(y))}
def calculat(x):
    x =x.split()
    a =[i for i, a in enumerate(x) if a in '/*']#find index operand
    while a:
        y = a[0]
        a,b,c = x[y - 1: y + 2]#depac expression
        x[y - 1: y + 2] = [actions[b](a,c)]
        a = [i for i, a in enumerate(x) if a in '/*']
    while len(x) > 1:
        a, b, c = x[: 3]
        x[: 3] = [actions[b](a,c)]
    return x[0]

print(calculat(input()))
