# Task 1


class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.know_list = []

    def know(self, person):
        if person not in self.know_list:
            self.know_list.append(person)
        else:
            print('{} уже знает человка по имени {}'.format(self.name, person.name))

    def is_know(self, person):
        text_answers = {True: "know this person", False: "don't know this person"}
        is_know_person = person in self.know_list
        print('{} {} {}'.format(self.name, text_answers[is_know_person], person.name))

    def show_person_list(self):
        for person in self.know_list:
            print(person.name, person.age)


person_vit = Person(25, 'Vitalii')
san = Person(36, 'Sasha')
nik = Person(30, 'Nick')
nick1 = nik

person_vit.know(san)
person_vit.know(nik)

person_vit.show_person_list()

person_vit.know(nick1)

person_vit.is_know(nick1)


# Task2

class Printer(object):
    def __init__(self):
        self.values = []

    def log(self, *values):
        self.values = [v for v in values]
        print(self.values)


class FormattedPrinter(Printer):

    def formated_log(self, *values):
        print('********************')
        self.log(*values)
        print('********************')


text = Printer()
text.log('qweeqweasdasdgdfgdfgfdg')

text1 = FormattedPrinter()
text1.log('qwertyqwertyqwertyqwery')
text1.formated_log('qwertyqwertyqwertyqwery')


# task3

class Animal(object):

    def __init__(self, name, aggressive):
        self.name = name
        self.aggressive = aggressive

    def attack_human(self, human):
        if self.aggressive and not human.aggressive:
            print('Атака {} на {} прошла успешно!'.format(self.name, human.name))
        else:
            print('Атака {} на {} не удалась!'.format(self.name, human.name))


class Human(Animal):

    def __init__(self, name, aggressive):
        self.name = name
        self.aggressive = aggressive
        self.dangerous_animals = []

    def is_dangerous(self, animal):
        answers = {True:'Yes', False: 'No'}
        return answers[animal in self.dangerous_animals]

hercules = Human('Геракл', True)
prometeus = Human('Prometeus', False)

hydra = Animal('Hydra', True)
hawk = Animal("Ястреб", True)
lamd = Animal('Овца', False)

hydra.attack_human(hercules)
hawk.attack_human(hercules)
lamd.attack_human(hercules)

hydra.attack_human(prometeus)
hawk.attack_human(prometeus)
lamd.attack_human(prometeus)


hercules.attack_human(hercules)
hercules.attack_human(prometeus)


print(hercules.is_dangerous(hydra))
print(prometeus.dangerous_animals)