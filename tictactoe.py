import random as rd


def help_me():
    print('''\nRULES FOR TIC-TAC-TOE

1. The game is played on a grid that's 3 squares by 3 squares.

2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.

3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

HOW CAN I WIN AT TIC-TAC-TOE?
To beat the computer (or at least tie), you need to make use of a little bit of strategy. Strategy means figuring out 
what you need to do to win.

Part of your strategy is trying to figure out how to get three Xs in a row. The other part is trying to figure out how 
to stop the computer from getting three Os in a row.

After you put an X in a square, you start looking ahead. Where's the best place for your next X? You look at the empty 
squares and decide which ones are good choices—which ones might let you make three Xs in a row.

You also have to watch where the computer puts its O. That could change what you do next. If the computer gets two Os in
 a row, you have to put your next X in the last empty square in that row, or the computer will win. You are forced to 
 play in a particular square or lose the game.

If you always pay attention and look ahead, you'll never lose a game of Tic-Tac-Toe. You may not win, but at least 
you'll tie.\n''')


def centres_and_edges(t):
    global pos_var, pos_var_copy

    centre_and_edges = [1, 3, 4, 5, 7]
    corner = [0, 2, 6, 8]
    empty_corner = []
    empty_edges = []

    for li in corner:
        if (pos_var[li] != 'X') and (pos_var[li] != 'O'):
            empty_corner.append(li)

    if len(empty_corner) == 0:
        flag = 1

    else:
        flag = 2

    if flag == 2:
        pos_var[rd.choice(empty_corner)] = "O"
        pos_var_copy = pos_var[:]

        return t + 1

    elif flag == 1:
        for m in centre_and_edges:
            if (pos_var[m] != 'X') and (pos_var[m] != 'O'):
                empty_edges.append(m)

        pos_var[rd.choice(empty_edges)] = "O"
        pos_var_copy = pos_var[:]

        return t + 1


def computer(t):
    global pos_var, pos_var_copy

    pos_var_copy = pos_var[:]
    blanks = []

    for j in range(len(pos_var)):
        if (pos_var[j] != 'X') and (pos_var[j] != 'O'):
            blanks.append(j)

    for k in blanks:
        pos_var_copy = pos_var[:]
        pos_var_copy[k] = 'O'

        if ((pos_var_copy[0] == pos_var_copy[1] == pos_var_copy[2]) or
                (pos_var_copy[3] == pos_var_copy[4] == pos_var_copy[5])
                or (pos_var_copy[6] == pos_var_copy[7] == pos_var_copy[8]) or
                (pos_var_copy[0] == pos_var_copy[3] == pos_var_copy[6])
                or (pos_var_copy[1] == pos_var_copy[4] == pos_var_copy[7]) or
                (pos_var_copy[2] == pos_var_copy[5] == pos_var_copy[8])
                or (pos_var_copy[0] == pos_var_copy[4] == pos_var_copy[8]) or
                (pos_var_copy[2] == pos_var_copy[4] == pos_var_copy[6])):

            pos_var[k] = 'O'

            return t - 1

    for l in blanks:
        pos_var_copy = pos_var[:]
        pos_var_copy[l] = 'X'

        if ((pos_var_copy[0] == pos_var_copy[1] == pos_var_copy[2]) or
                (pos_var_copy[3] == pos_var_copy[4] == pos_var_copy[5])
                or (pos_var_copy[6] == pos_var_copy[7] == pos_var_copy[8]) or
                (pos_var_copy[0] == pos_var_copy[3] == pos_var_copy[6])
                or (pos_var_copy[1] == pos_var_copy[4] == pos_var_copy[7]) or
                (pos_var_copy[2] == pos_var_copy[5] == pos_var_copy[8])
                or (pos_var_copy[0] == pos_var_copy[4] == pos_var_copy[8]) or
                (pos_var_copy[2] == pos_var_copy[4] == pos_var_copy[6])):

            pos_var[l] = 'O'

            return t + 1

    pos_var_copy = pos_var[:]
    t = centres_and_edges(t)

    return t


def update_2(pos, t):
    global pos_var

    if t % 2 == 1 and (pos_var[pos - 1] != "X" and pos_var[pos - 1] != "O"):
        pos_var[pos - 1] = "X"

    elif t % 2 == 0 and (pos_var[pos - 1] != "X" and pos_var[pos - 1] != "O"):
        pos_var[pos - 1] = "O"

    elif pos_var[pos - 1] == "X" or pos_var[pos - 1] == "O":
        t = t - 1
        print("THIS POSITION IS ALREADY MARKED, TRY AGAIN!")

    print(f'''[{pos_var[0]}] [{pos_var[1]}] [{pos_var[2]}]
[{pos_var[3]}] [{pos_var[4]}] [{pos_var[5]}]
[{pos_var[6]}] [{pos_var[7]}] [{pos_var[8]}]\n''')

    return t


def update_1(pos, t):
    global pos_var, win

    if t % 2 == 1 and (pos_var[pos - 1] != "X" and pos_var[pos - 1] != "O"):
        pos_var[pos - 1] = "X"
        win_check(t+1)

        if t != 9 and win == 0:
            t = computer(t)

    elif pos_var[pos - 1] == "X" or pos_var[pos - 1] == "O":
        t = t - 1
        print("THIS POSITION IS ALREADY MARKED, TRY AGAIN!")

    print(f'''[{pos_var[0]}] [{pos_var[1]}] [{pos_var[2]}]
[{pos_var[3]}] [{pos_var[4]}] [{pos_var[5]}]
[{pos_var[6]}] [{pos_var[7]}] [{pos_var[8]}]\n''')

    return t


def win_check(t):
    global win, pos_var

    if (pos_var[0] == pos_var[1] == pos_var[2]) or (pos_var[3] == pos_var[4] == pos_var[5]) \
            or (pos_var[6] == pos_var[7] == pos_var[8]) or (pos_var[0] == pos_var[3] == pos_var[6]) \
            or (pos_var[1] == pos_var[4] == pos_var[7]) or (pos_var[2] == pos_var[5] == pos_var[8]) \
            or (pos_var[0] == pos_var[4] == pos_var[8]) or (pos_var[2] == pos_var[4] == pos_var[6]):
        win = 1

        if t % 2 == 1:
            print("X (PLAYER 1) WINS!!!")
            return 1

        elif t % 2 == 0:
            print("O (PLAYER 2) WINS!!!")
            return 1

    elif t == 9 and win == 0:
        print("It's a draw!!!")
        return 1

    else:
        return 0


def one_player():
    winner = 0
    t = 1

    print('NOTE:Player1 uses symbol "X".\nPlayer1 goes first!')

    print(f'''[{a}] [{b}] [{c}]
[{d}] [{e}] [{f}]
[{g}] [{h}] [{i}]\n''')

    while winner != 1:
        pos = int(input("On what position would you like to mark your symbol?: "))
        t = update_1(pos, t)
        winner = win_check(t)
        t = t + 1


def two_player():
    winner = 0
    t = 1

    print('\nPlayer1 uses symbol "X". Player1 goes first!')

    print(f'''[{a}] [{b}] [{c}]
[{d}] [{e}] [{f}]
[{g}] [{h}] [{i}]\n''')

    while winner == 0:
        pos = int(input("On what position would you like to mark your symbol?: "))
        t = update_2(pos, t)
        winner = win_check(t)
        t = t + 1


state = ''
player1 = 'X'
player2 = 'O'
helped = 0
num_players = 0
win = 0
a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9
pos_var = [a, b, c, d, e, f, g, h, i]
pos_var_copy = [a, b, c, d, e, f, g, h, i]

while state.upper() != "START":

    state = input('''Enter: START to start the game OR
Enter: HElP for instructions\n\n''')

    if state.upper() == "HELP" and helped == 0:
        help_me()
        helped = 1

    elif state.upper() == "HELP" and helped == 1:
        print("Help Already Received, Duh!!!\n")

    elif state.upper() == "START":

        while num_players != 1 and num_players != 2:
            num_players = int(input("\nEnter the number of players (1 or 2): "))

            if num_players == 1:
                one_player()

            elif num_players == 2:
                two_player()

            else:
                print("Sorry, Please try entering '1' or '2'")

    else:
        print('Please try again: ')
