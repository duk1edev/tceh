# Замыкания


def outer_function(value):
    def some_inner():
        print('Value was ', value)
    return some_inner


v = outer_function('some')
print('it is a function', v, callable(v))
v()

