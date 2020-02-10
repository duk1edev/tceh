# Пользователь вводит список чисел через пробелб если ввел
# 1 число строим квадрат
# 2 числа строим прямоугольник
# 3 числа строим трехугольник
# 4 строим многоугольник
#
#   Вычисляем площадь, перимет  и выводим в консль
#   провеки на воозможность пострить фигуру с данными сторонами


class Figure(object):
    def __init__(self, *values):
        self.values = list(values)
        print(self.values)
        if len(values) == 1:
            print("This is square!")
        if len(values) == 2:
            print('This is rectangle')
        if len(values) == 3:
            print('This is triangle')


def perimetr(*value):
    pass

def square(*values):
    pass


get_user_input = input("Enter the number: ")
square = Figure()



