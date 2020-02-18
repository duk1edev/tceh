import functools

class MyDecorator(object):
    def __init__(self, argument):
        self.arg = argument

    def __call__(self, fn):
        @functools  .wraps(fn)
        def decorated(*args, **kwargs):
            print('Im my decoration before call, with arg {}'.format(self.arg))
            fn(*args, **kwargs)
            print("in my decorator after call, with arg {}".format(self.arg))
        return decorated

class Foo(object):
    @MyDecorator("in foo class!")
    def bar(self):
        print("in bar!")


@MyDecorator("some other func!")
def some_other_functions():
    print("in some other function")


Foo().bar()
some_other_functions()