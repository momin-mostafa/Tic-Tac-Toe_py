def board(b):
    print(f" {b[0]} | {b[1]} | {b[2]}")
    print('-----------')
    print(f" {b[3]} | {b[4]} | {b[5]}")
    print('-----------')
    print(f' {b[6]} | {b[7]} | {b[8]}')


def as_to_b(inp):
    if inp == 1:
        b[0] = player_input
    elif inp == 2:
        b[1] = player_input
    elif inp == 3:
        b[2] = player_input
    elif inp == 4:
        b[3] = player_input
    elif inp == 5:
        b[4] = player_input
    elif inp == 6:
        b[5] = player_input
    elif inp == 7:
        b[6] = player_input
    elif inp == 8:
        b[7] = player_input
    elif inp == 9:
        b[8] = player_input
    else:
        print('not recognised')


def player_i(count):
    if count in even:
        global player_input
        player_input = 'X'
    else:
        player_input = 'Y'


def win_cheak(b):
    global win
    p = 'player One won the game'
    p2 = 'player Two won the game'
    if b[0] == 'X' and b[1] == "X" and b[2] == 'X':
        print(p)
        win = 1
    elif b[3] == 'X' and b[4] == 'X' and b[5] == 'X':
        print(p)
        win = 1
    elif b[6] == 'X' and b[7] == 'X' and b[8] == 'X':
        print(p)
        win = 1
    elif b[0] == 'X' and b[4] == 'X' and b[8] == 'X':
        print(p)
        win = 1
    elif b[6] == 'X' and b[4] == 'X' and b[2] == 'X':
        print(p)
        win = 1
    elif b[0] == 'X' and b[3] == 'X' and b[6] == 'X':
        print(p)
        win = 1
    elif b[1] == 'X' and b[4] == 'X' and b[7] == 'X':
        print(p)
        win = 1
    elif b[2] == 'X' and b[5] == 'X' and b[8] == "X":
        print(p)
        win = 1
    elif b[0] == 'Y' and b[1] == "Y" and b[2] == 'Y':
        print(p2)
        win = 1
    elif b[3] == 'Y' and b[4] == 'Y' and b[5] == 'Y':
        print(p2)
        win = 1
    elif b[6] == 'Y' and b[7] == 'Y' and b[8] == 'Y':
        print(p2)
        win = 1
    elif b[0] == 'Y' and b[4] == 'Y' and b[8] == 'Y':
        print(p2)
        win = 1
    elif b[6] == 'Y' and b[4] == 'Y' and b[2] == 'Y':
        print(p2)
        win = 1
    elif b[0] == 'Y' and b[3] == 'Y' and b[6] == 'Y':
        print(p2)
        win = 1
    elif b[1] == 'Y' and b[4] == 'Y' and b[7] == 'Y':
        print(p2)
        win = 1
    elif b[2] == 'Y' and b[5] == 'Y' and b[8] == "Y":
        print(p2)
        win = 1
    else:
        pass


print('welcome to python tic tac toe game.')
b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board(b)

count = 0
even = [0, 2, 4, 6, 8]
lst_pl = 0
player_input = ''
win = 0

while count != 9 and win == 0:
    if count in even:
        pl_1 = int(input('please enter a position (1-9)'))
        player_i(count)
        as_to_b(pl_1)
        win_cheak(b)
        board(b)
        count += 1
    else:
        pl_2 = int(input('please enter a position (1-9)'))
        player_i(count)
        as_to_b(pl_2)
        win_cheak(b)
        board(b)
        count += 1
