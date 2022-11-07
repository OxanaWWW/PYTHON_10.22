# **********1****************
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def some_words(text):
    # text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join([i for i in text.split() if 'abv' not in i])


print(some_words(input()))

# ********************2*********************
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

from random import shuffle, randint

all_amount = 120
max_sweet = 28
a = int(input('play kid - 1 or bot - 0?'))
players = ['person', 'kid' if a else 'bot']
shuffle(players)
aktiv_player = players[0]
print(f'fierst in game {players[0]},second in game {players[1]}')


def game_bot():
    result = all_amount % 29
    if not result:
        result = randint(1, 28)
    return result


def all_game(s):
    f_1, f_2 = players
    return f_2 if s == f_1 else f_1


while all_amount > 0:
    print(f'all sweet {all_amount} and limit {max_sweet} ')
    if aktiv_player == 'bot':
        x = game_bot()
        print(f'bot take {x}')
    else:
        x = int(input(f' take sweet  {aktiv_player}'))
    if x not in range(1, max_sweet + 1):
        print(f' thats mistake')
    else:
        all_amount -= x
        if all_amount > 0:
            aktiv_player = all_game(aktiv_player)
        else:
            print(f' you winner {aktiv_player}')

##******************3****************
# Создайте программу для игры в ""Крестики-нолики"".
board = list(map(str, range(1, 10)))


def game_board():
    print("-" * 11)
    for i in range(3):
        for e in range(3):
            print(f'{board[e + i * 3]} |', end=' ')

        print('\n' + "-" * 11)


def enter_X0(y):
    global board
    while True:
        a = input(' Check number from 1 till 9    ')
        if a.isdigit() and int(a) in range(1, 10):
            if board[int(a) - 1] not in 'X0':
                board[int(a) - 1] = 'X' if y == 'X' else '0'
                break
            else:
                print(' place closed')
        else:
            print('incorrect  try agein')


def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main_game():
    count = 0
    game_board()
    while True:

        enter_X0('X') if count % 2 == 0 else enter_X0('0')
        count += 1
        game_board()
        if count > 4:
            tmp = check_win()
            if tmp:
                print(tmp, "выиграл!")
                break
        if count == 9:
            print(' no winner')
            break


main_game()

# ************4************
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def RLE_decod(x):
    a = ''
    count = 1
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            count += 1
        else:
            a += f'{count}{x[i]}'
            count = 1
    return a


print(RLE_decod(input()))
