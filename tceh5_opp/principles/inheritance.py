class Parent(object):
    field = 'some field'

    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'

    def do(self):
        print('Parent do(): {}'.format(self.value))


class Child(Parent):
    # field = 'child field'

    def __init__(self):
        print('Child inited')
        self.value = 'Child'



parent = Parent()
parent.do()
print(parent.field)

child = Child()
child.do()
print(child.field)