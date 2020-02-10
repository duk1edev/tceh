class Example(object):
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 4
        print('{} {} {} '.format(self.a, self._b, self.__c))

    def call(self):
        print('called!!!!')


example = Example()
print(example.a)
print(example.b)
try:
    print(example.__c)
except AttributeError as e:
    print("Error: ", e)

