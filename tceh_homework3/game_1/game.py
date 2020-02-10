import random

EMPTY_MARK = 'x'

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space
    """

    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)

    return field


def print_field(field):
    """This method prints field to user.
    :param field: current field state to be printed
    :return: None
    """
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True is the game is finished, False otherwise.
    """

    ideal = list(range(1, 16))
    ideal.append(EMPTY_MARK)
    return ideal == field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state(after the move).
    :raises: IndexError if the move can't be done.
    """

    current_position = field.index(EMPTY_MARK)

    if key == 's' and current_position >= 12:
        raise IndexError('Cant move down')
    if key == 'd' and current_position % 4 == 3:
        raise IndexError('Cant move right')
    if key == 'w' and current_position < 4:
        raise IndexError('Cant move up')
    if key == 'a' and current_position % 4 == 0:
        raise IndexError('Cant move left')

    delta = MOVES[key]

    field[current_position], field[current_position + delta] = field[current_position + delta], field[current_position]

    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move
    """

    while True:
        user_move = input('Please, input your move: ')
        if user_move in MOVES.keys():
            return user_move


def main():
    """
    The main method. It starts whe the program is called.
    It also calls other methods.
    :return: None
    """

    field = shuffle_field()
    # field = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,x]

    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError as e:
            print(e)

    print('Game is finished!!!')


if __name__ == '__main__':
    main()