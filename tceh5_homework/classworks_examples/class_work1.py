class HandBox(object):
    def __init__(self, size):
        self.size = size

    def change_size(self, size):
        self.size = size

    def get_size(self):
        print('This HandBox size = {}'.format(self.size))

    def put_something(self, item):
        if item.size <= self.size:
            print('{} is in a HandBox'.format(item))
        else:
            print('{} is to big for a HandBox with size {}!'.format(item, self.size))


class Bag(HandBox):
    def get_size(self):
        print('This  Bag size = {}'.format(self.size))

    def put_something(self, item):
        if item.size <= self.size:
            print('{} is in a Bag'.format(item))
        else:
            print('{} is to big for a Bag with size = {} '.format(item, self.size))


class Thing(object):
    def __init__(self,size):
        self.size = size


box1 = HandBox(20)
box1.get_size()

bag1 = Bag(130)
bag1.get_size()

item1 = Thing(10)
item2 = Thing(50)
item3 = Thing(150)

box1.put_something(item1)
box1.put_something(item2)
box1.put_something(item3)

bag1.put_something(item1)
bag1.put_something(item2)
bag1.put_something(item3)




