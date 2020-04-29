print("Hello");
from functools import wraps, reduce
from time import time
# Decorators

def canceler(func):

    @wraps(func)
    def cancel_wrap(*args, **kwargs):
        return '{} is canceled!'.format(func.__name__)

    return cancel_wrap


def timer(func):

    @wraps(func)
    def timer_wrap(*args,**kwargs):
        start = time()
        func_return = func(*args, **kwargs)
        end = time()
        print('{} is working for {} seconds'.format(func.__name__,(end-start)))

    return timer_wrap

def logger(func):
    print('Decorator created\n')

    @wraps(func)
    def logger_wrap(*args, **kwargs):

        print('\n1.\'{}\' started\n'.format(func.__name__))
        func_return = func(*args, **kwargs)
        print('2.\'{}\ stopped\n'.format(func.__name__))

        return func_return

    return logger_wrap



def catcher(func):

    @wraps(func)
    def catcher_wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return 'Exception \'{}\' occured while  running \'{}\''.format(e, func.__name__)
    return catcher_wrap


class Counter(object):

    @staticmethod
    def call_counter(func):

        def counter_wrap(*args, **kwargs):
            if func.__name__ in Counter.instances.keys():
                Counter.instances[func.__name__] += 1
            else:
                Counter.instances[func.__name__] = 1
        print('{} is called {} times'.format(func.__name__, Counter.instances[func.__name__]))

        return func(*args, **kwargs)

    return counter_wrap


# ОРИГИНАЛЬНЫЕ ФУНКЦ
@Counter.call_counter
@canceler
def long(value):
    import time
    time.sleep(5)

    return 'long_'  + str(value)


@Counter.call_counter
@logger
def short(string_param):
    print('Speed!', string_param)
    return 'short'

@Counter.call_counter
@timer
def medium(value, *modificators):
    result = value
    for m in modificators:
        ressult *= m

    return ressult

@Counter.call_counter
@catcher
def change_sign(num, check_sing=True):
    if check_sing and num > 0:
        raise ValueError('num > 0')
    return -num


def main():

    print('***** TASK 7 part 1 *** Decorators ***\n')
    print(long(300))
    print(long(3))
    print(long(14))
    print(long(1))
    print('\n********************')

    print('\n****************************')
    print(medium(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(medium(1, 2, 3, 4, 5, 6, 7))

    print('\n****************')
    print(short('Hi'))
    print(short('Bye'))

    print('\n*****************************')
    print(change_sign(15, True))
    print(change_sign(15, False))
    print(change_sign(-115, True))

    print('\n*************************')

    print('**** TASK 7 part 2 *** MAP/FILTER/REDUCE/lambda ***\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
