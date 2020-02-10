class Car:
    pass

c = Car()

print(c, type(c))

# Classes can have variable called fields

class Room:
    number = 'Room 34'
    floor = 4

r = Room()
r1 = Room()
print(r.number, r1.number)
print(r.floor, r1.floor)

# You can modify values:
r.number = 32
r.floor = '5 floor'

print(r.number, r1.number)
print(r.floor, r1.floor)


# Classes can have functions inside: it's called method:

class Car:
    speed = 0

    def accelerate(self):
        self.speed = self.speed + 3

    def accelerate(self, speed_delta):
        self.speed = self.speed + speed_delta

    def stop(self):
        self.speed = self.speed - 3


car1 = Car()
car1.speed = 60
print("Speed = ", car1.speed)
car1.accelerate(34)
print("Speed = ", car1.speed)
car1.stop()
print("Speed = ", car1.speed)

def foo():
    pass


class Door:
    def __init__(self):
        self.opened = True

    def open(self):
        print('self is', self)
        print('Door os opened!')


d = Door()
d.open()

d1 = Door()
d1.open()


# Methods can accept params(as function)

class Terminal:
    def hello(self, user_name):
        print('self is the object itself', self)
        print('Hello', user_name)


t = Terminal()
t.hello('Nikita')
t.hello('BVVAdfsdfa')


# Classes can have both methods and fields

class Window:
    is_opened = False

    def open(self):
        self.is_opened = True
        print('Window is now', self.is_opened)

    def close(self):
        self.is_opened = False
        print('Windows is now', self.is_opened)


w = Window()
w1 = Window()

print('Initial state', w.is_opened, w1.is_opened)

w.open()

print('New state, ', w.is_opened, w1.is_opened)