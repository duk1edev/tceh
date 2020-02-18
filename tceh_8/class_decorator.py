def time_this(original_function):
    def new_function(*args, **kwargs):
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after - before))
        return x

    return new_function


class ImportantStuff:
    @time_this
    def do_stuff_1(self):
        pass

    @time_this
    def do_stuff_2(self):
        pass

    @time_this
    def do_stiff(self):
        pass


def time_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            """
            this is called whenever any attribute of a NewCls object is accesed. This function
            first tries to get attribute off NewCls. If it fails then it tries to fetch the attribute from
            self.oInstance ( an instance of decorated class). if it manages to fetch the attribute from
            self.oInstance, and the attribute is an instance method then 'time_this' is applied.
            """
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x


            if type(x) == type(self.__init__):
                return time_this(x)
            else:
                return x

    return NewCls


@time_all_class_methods
class ImportantStuff:
    def do_stuff_1(self):
        pass

    def do_stuff_2(self):
        pass

    def do_stuff_3(self):
        pass


@time_all_class_methods
class Foo(object):

    def a(self):
        print("entering a")
        import time
        time.sleep(3)
        print('exiting a ')


oF = Foo()
oF.a()
