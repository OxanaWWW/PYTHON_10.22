# **********1*********
number_day = int(input())
if number_day <= 5:
    print('day_on')
else:
    if number_day == 6 or 7:
        print('day_off')

# **********2***********

x = int(input())
y = int(input())
z = int(input())

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not (x or y or z) == (not x and not y and not z))
print(x, y, z)
#
#**************3**********

x = int(input('Введите число x≠0:'))
y = int(input('Введите число y≠0:'))
if x > 0 and y > 0:
    print({f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 '})
elif x < 0 and y > 0:
    print({f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 '})
elif x < 0 and y < 0:
    print({f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 '})
else:
    print({f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 '})

# # ********4*********
x = int(input('Enter quater:  '))
if x == 1:
    print('x > 0 and y > 0')
if x == 2:
    print('x < 0 and y > 0')
if x == 3:
    print('x < 0 and y < 0')
if x == 4:
    print('x > 0 and y < 0')



# ***********5**************
#
from math import *

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print("Расстояние между точками : ", round(sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2), 2))


