import random

EMPTY_MARK = 'x'

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1
}


def shuffle_field():
    field = list(range(1, 16))
    field.append(EMPTY_MARK)
    random.shuffle(field)

    # possible_moves = list(MOVES.keys())
    # allied_moves = 0
    # while allied_moves < 100:
    #     random_move = random.choice(possible_moves)
    #
    #   try:
    #        field = perform_move(field, random_move)
    #       allied_moves += 1
    #   except IndexError:
    #       continue

    return field


def print_field(field):
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


def is_game_finished(field):
    ideal = list(range(1, 16))
    ideal.append(EMPTY_MARK)

    return ideal == field


def perform_move(field, key):
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


def handle_user_input():
    while True:
        user_move = input('Please, make your move: ')
        if user_move in MOVES.keys():
            return user_move


def main():
    field = shuffle_field()
    # field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'x', 15]

    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            perform_move(field, move)
        except IndexError as e:
            print(e)
    print('Game is finished')


if __name__ == '__main__':
    main()
