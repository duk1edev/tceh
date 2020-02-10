# We can expand lists and dicts


def accepts_args(*args):
    print(args)
    return sum(args)


accepts_args(0, 1, 2, 3, 4)

values = [1, 4, 9, 3]

try:
    accepts_args(values)
except TypeError as e:
    print('Error: ', e)

accepts_args(*values)

# kwargs is the same


def accepts_kwargs(**kwargs):
    print(kwargs)


accepts_kwargs(name='Vvv', job='dev')

values = {'day': 'wed', 'month': 'may'}

try:
    accepts_kwargs(values)
except TypeError as e:
    print('Error: ', e)

accepts_kwargs(**values)

