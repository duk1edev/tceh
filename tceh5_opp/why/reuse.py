def main_function(obj):
    param = 34
    return obj.do_something(param)


class SomeOldLogic:
    def do_something(self, value):
        x = self.calc(value)
        # some strange logic
        return 0

    def calc(self, value):
        return value * 7 + 90


x = SomeOldLogic()
main_function(x)

class NewLogic(SomeOldLogic):
    def calc(self, value):
        return value + 2


y = NewLogic()
main_function(y)

