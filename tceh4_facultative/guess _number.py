import random


def create_number():
    """
    This function create random number.
    :return: random number
    """
    return random.randint(1, 15)


def get_user_input():
    while True:
        number = input('Please, guess the number: ')
        if not number.isnumeric():
            print('Incorrect input, need enter the number')
        else:
            print('Your number is : ', number)
            break
    return int(number)


def main():
    number = create_number()
    current_errors = 10
    print(number)

    print('Guess the number!!!')
    while current_errors > 0:
        user_number = get_user_input()
        if user_number == number:
            print('You win!')
            break
        else:
            print('You not guess!Repeat again...')
            current_errors -= 1
            print('Errors left,', current_errors)
    print('Finish')


if __name__ == '__main__':
    main()
