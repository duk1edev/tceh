# ЗАДАЧА С КУРСА ДЕНЬ 5
# пользователь вводит список чисел через пробел. если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, треугольник
# 4 числа, многоугольник
#
# вычисляем периметр и площадь. выводим в консоль.
# можно сделать проверки на "возмонжость" построить данную фигуру с такими сторонами.


import math


class Shape(object):
    def __init__(self, *sides):
        sides_qty = len(sides)

        if (sides_qty < 1) and (sides_qty > 4):
            raise ValueError('Ошибка при простоении фигуры. Количество сторон {}, '
                             'должно быть от 1 до 4.'.format(sides_qty))
        else:
            if sides_qty == 1:
                self.sides = [n for n in sides] * 4
            elif sides_qty == 2:
                self.sides = [n for n in sides] * 2
            else:
                self.sides = [n for n in sides]

    def _calc_per(self):
        return sum(self.sides)

    def print_sides(self, comment='Стороны фигуры'):
        print(comment, ':', self.sides)

    def print_per(self, figure_name="фигуры"):
        print('Периметр {} = {}'.format(figure_name, self._calc_per()))


class Rectangle(Shape):
    def _calc_sqr(self):
        return self.sides[0] * self.sides[1]

    def print_sqr(self):
        print('Площадь прямоугольника = {}'.format(self._calc_sqr()))


class Square(Rectangle):
    def print_sqr(self):
        print("Площадь квадрата = {} ".format(self._calc_sqr()))


class Triangle(Shape):
    def __init__(self, *sides):

        sides_qty = len(sides)

        if sides_qty != 3:
            raise ValueError('Ошибка при инициализации треугольника! Кол-во сторон {},'
                             'must have 3'.format(sides_qty))
        else:
            self.sides = [n for n in sides]

        self.sides.sort()

        larger_side = self.sides[len(self.sides) - 1]
        two_sides_sum = self.sides[0] + self.sides[1]

        if two_sides_sum <= larger_side:
            raise ValueError('Ошибка при инициализации треугольника!Со сторонамм такой длины сторон построить трехугольник'
                             'невозможно!')

    def _calc_sqr(self):
        half_per = self._calc_per() / 2
        return math.sqrt(half_per * (half_per - self.sides[0]) * (half_per - self.sides[1])) * (half_per - self.sides[2])

    def print_sqr(self):
        print('Площадь треугольника  = {}'.format(self._calc_sqr()))


class Polygon(Shape):
    def __init__(self, *sides):
        sides_qty = len(sides)

        if sides_qty != 4:
            raise ValueError('Ошибка при инициализации четырехугольника! Кол-во сторон {}, а должно быть 4'.format(sides_qty))
        else:
            self.sides = [n for n in sides]

        self.sides.sort()

        larger_side = self.sides[len(self.sides) - 1]

        three_sides_sum = self.sides[0] + self.sides[1] + self.sides[2]

        if three_sides_sum <= larger_side:
            raise ValueError('Ошибка при инициализцаии четырех угольник!Со стронами такой длины'
                             'построить четырех угольник не возможно')

    def _calc_sqr(self):
            return 'Расчитать площадь произвольного четырех угольника без знания двух углов не возможно'

    def print_sqr(self):
            print(self._calc_sqr())


rect = Rectangle(1,2)
rect.print_sides('Стороны прямоугольника')
rect.print_per('прямоугольник')
rect.print_sqr()
