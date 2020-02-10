class Calc(object):
    def __init__(self, value):
        print('Calc constructor is called')
        self.value = value

    def count(self):
        return self.value * 8 + 9


class DoubleCalc(Calc):
    def count(self):
        return 2 * super().count()


class ExtentedCalc(DoubleCalc):
    def __init__(self, value, k=1):
        super().__init__(value)
        print('Extender', self.value)

        self.k = k

    def count(self):
        a = self.k + 1
        previous = super().count()
        # previous = self.value * 8 + 9
        return -1 * self.k * previous


e = ExtentedCalc(8, k=1.2)
print(e.count())

