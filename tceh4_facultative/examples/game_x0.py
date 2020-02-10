# Game x - 0
import random

EQ_X = 'X'
EQ_O = 'O'
EMPTY = ' '
COUNT = 9


def create_board():
    """
    Creating game board
    ":return: game board
    """
    board = []
    for i in range(COUNT):
        board.append(EMPTY)
    return board


def print_board(board):
    """
    Printing the game board
    :param board:
    :return: None
    """
    print('\n\t', board[0], "|", board[1], "|", board[2])
    print('\t', "---------")
    print('\n\t', board[3], "|", board[4], "|", board[5])
    print('\t', "---------")
    print('\n\t', board[6], "|", board[7], "|", board[8], '\n')


def choose_the_side():
    """
    Choose who will play x  or 0
    :return:
    """
    answer = None
    while answer not in ("y", "n"):
        answer = input("You want to start first? (Y/n):")
        if answer == "y":
            human = EQ_X
            computer = EQ_O
        else:
            human = EQ_O
            computer = EQ_X
    return human, computer


def legal_moves(board):
    """
    Create a list of legal moves
    :param:
    :return:
    """
    result = []
    for i in range(COUNT):
        if board[i] == EMPTY:
            result.append(i)
    return result


def next_turn(turn):
    """
    Change the turn from x to 0, from 0 to x
    :param turn:
    :return:
    """
    if turn == EQ_X:
        return EQ_O
    else:
        return EQ_X


def human_step(board):
    """
    Make the human step
    :param board: board
    :return: field
    """
    step = None
    moves = legal_moves(board)

    while step not in moves:
        step = int(input("Your move. Field from 0 to 8: \n"))
        if step not in moves:
            print('This is field not empty, choose another one')
    return step


def computer_step(board, computer, human):
    """
    Getting computer step
    :param board:
    :return:
    """
    board = board[:]
    print('Computer step')
    for s in legal_moves(board):
        board[s] = computer
        if winner(board) == computer:
            print(s)
            return s
    for s in legal_moves(board):
        board[s] = human
        if winner(board) == human:
            print(s)
            return s
        board[s] = EMPTY
    step = random.choice(legal_moves(board))
    print(step)
    return step


def winner(board):
    """
    Choose winner
    :param board: board
    :return: winner
    """

    WAYS_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )

    for i in WAYS_WIN:
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY:
            winner = board[i[0]]
            return winner
    if EMPTY not in board:
        s = 'Draw'
        return s


def main():
    """
    Starting game
    :return:
    """
    print("""
    Game x - 0, with computer \n
    To make step, enter the number from 0 - 8.
    The number like on the picture.
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8    
    """)
    human, computer = choose_the_side()
    turn = EQ_X
    board = create_board()
    print_board(board)
    while not winner(board):
        if turn == human:
            step = human_step(board)
            board[step] = human
        else:
            step = computer_step(board, computer, human)
            board[step] = computer
        print_board(board)
        turn = next_turn(turn)
        theWinner = winner(board)
    if theWinner == computer:
        print("Computer wins!")
    elif theWinner == "Draw":
        print("Draw")
    else:
        print("You win!")


if __name__ == '__main__':
    main()
    input('Press enter to exit')
