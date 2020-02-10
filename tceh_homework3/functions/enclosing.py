# Functions can use a global variables

GLOBAL_VAR = 3


def using_global(x):
    print(x * GLOBAL_VAR)


using_global(25)

# But if we want to write to it, we shold state it explicitly


def writing_to_global_var(value):
    global GLOBAL_VAR
    GLOBAL_VAR = value
    print('it is now', GLOBAL_VAR)


writing_to_global_var(25)

# Functions are objects and can ne nested


def outer_functions(value):
    def some_inner():
        print('Value has', value)
    return some_inner()


v = outer_functions('some')
print('it is calling outer_function', v, callable(v))
