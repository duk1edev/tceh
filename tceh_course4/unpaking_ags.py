def accepts_args(*args):
    print(args)
    return sum(args)


accepts_args(1, 23, 32, 0)
values = [1, 2, 9, 3]

try:
    accepts_args(values)
except TypeError as e:
    print('Error: ', e)

accepts_args(*values)


# The same for kwargs:

def accepts_kwargs(**kwargs):
    print(kwargs)


accepts_args(name='Vitalii', job='dev')

values = {'day': 'wed', 'month': 'may'}

try:
    accepts_args(values)
except TypeError as e:
    print('Error', e)

accepts_args(**values)
