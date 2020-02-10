class TestClass:
    def __init__(self):
        print('Constructor is called')
        print('Self is the object itself', self)


t = TestClass()
t1 = TestClass()


class Car:
    engine = 'V8 turbo'

    def __init__(self, requested_color):
        self.color = requested_color


t = Car('red')
print(t.color)
t1 = Car('white')
print(t1.color)


class Table:
    def __init__(self, number_of_legs):
        print('New table has {} legs'.format(number_of_legs))


t = Table(4)
t1 = Table(5)


class Chair:
    def __init__(self, color):
        self.color = color


c = Chair('green')
print(c, c.color)

c1 = Chair('Red')
print(c1.color)
print('variable c did not change', c.color)

