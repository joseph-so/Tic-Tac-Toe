# write your code here
board = [[" "] * 3 for i in range(3)]


def print_board():
    print("---------")
    for i in range(3):
        print("|", end=' ')
        for j in range(3):
            print(board[j][2 - i], end=" ")
        print("|")
    print("---------")


def move(turn):
    global board
    valid_move = False
    while not valid_move:
        x, y = input("Enter the coordinates: ").split()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if 1 <= x <= 3 and 1 <= y <= 3:
                if board[x - 1][y - 1] == " ":
                    board[x - 1][y - 1] = turn
                    valid_move = True
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


def draw_game():
    space = sum([r.count(' ') for r in board])
    if space == 0:
        print('Draw')
        return True
    else:
        return False


def win_game(turn):
    win = any([
        any([sum(item == turn for item in r) == 3 for r in board]),
        any([board[0][i] == board[1][i] == board[2][i] == turn for i in range(3)]),
        board[0][0] == board[1][1] == board[2][2] == turn,
        board[0][2] == board[1][1] == board[2][0] == turn
    ])

    if win:
        print(f'{turn} wins')

    return win


x_turn = False
print_board()
while not (any([draw_game(), win_game('X' if x_turn else 'O')])):
    x_turn = not x_turn
    move('X' if x_turn else 'O')
    print_board()
