# 1. Создать класс корзина  у кторого можно выставить разную вмесительность
# для разных обьектов. В обект можн опомещать разные
# 2. Создать класс - пакет  в кторый тожно можн опомещать предмет у него тоже есть вместимость
# 3. Любой класс что бы можно было помещать в корзину и в пакет
# 4. Если вместимоть не достаточна сказать, что обьект поместить нельзя


class Trash:
    def __init__(self, set_size):
        self.size = set_size

    def get_obj(self, obj):
        if obj.size > self.size:
            print('You could not put this stuff({} size) to that trash, \n'
                  'trash size is {}'.format(obj.size, self.size))
        else:
            print('You put the {} size {} to the trash'.format(obj, obj.size))


class Packet(Trash):
    def __init__(self, set_size):
        self.size = set_size

    def get_obj(self, obj):
        if obj.size > self.size:
            print('You could not put this stuff({} size) to that packet, \n'
                  'packet size is {}'.format(obj.size, self.size))
        else:
            print('You put the {} size {} to the packet'.format(obj, obj.size))


class SomeStuff:
    def __init__(self, set_size):
        self.size = set_size


small_trash = Trash(5)
middle_trash = Trash(10)
big_trash = Trash(50)

small_packet = Packet(3)
middle_packet = Packet(5)
big_packet = Packet(10)

apple = SomeStuff(25)
print(apple.size)

garbage = SomeStuff(50)

small_trash.get_obj(apple)

big_trash.get_obj(garbage)
big_packet.get_obj(garbage) 