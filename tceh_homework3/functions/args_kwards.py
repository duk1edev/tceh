# Functions can receive keyword argument


def has_keyword(my=True, name='Computer'):
    if my:
        print('My', name)
    else:
        print('Not mine, ', name)


has_keyword(False, name='Sandwich')
has_keyword()


# Functions can receive unlimited number of positional arguments

def has_args(*args):
    print('A lot of arguments: ', args)


has_args(1, (23, 43, 234), 12, ['str', 'asdtesfsdf'], 3.14)


# Functions can receive unlimited number of keyword arguments


def has_kwargs(**kwargs):
    print('A lot of keywords arguments', kwargs)
    print('kwargs is a dict', type(kwargs))


has_kwargs(any_posiible='hello', words='words', values=[], you_wish=1)

# Functions that will cover 100% of arguments


def send_anything(*args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)


send_anything(1, 32, 'as', values='asdasd', securedis='keywords')

