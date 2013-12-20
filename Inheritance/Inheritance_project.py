class TestAnimal(object):

    def __init__(self):
        self.mouse = Mouse()
        self.lion = Lion()
        self.jackal = Jackal()
        self.rabbit = Rabbit()
        self.snail = Snail()

    def test_talk(self):
        assert self.mouse.talk() == 'Squeak!'
        assert self.lion.talk() == 'Rawr!'
        assert self.jackal.talk() == 'Woof! Woof!'
        assert self. rabbit.talk() == 'Sniff Sniff!'
        assert self.snail.talk() == 'Squeak'


    def test_hunt(self):
        assert self.mouse.alive == True
        self.rabbit.hunt(self.mouse)
        assert self.mouse.alive == False
        assert self.lion.alive == True
        self.rabbit.hunt(self.lion)
        assert self.lion.alive == True


class Animal(object):
    def __init__(self):
        self.alive = True

    def talk(self):
        raise NotImplementedError

    def hunt(self):
        raise NotImplementedError


class Lion(Animal):
    def talk(self):
        if self.alive:
            return 'Rawr!'

    def hunt(self, animal):
        if animal.__class__.__name__ == 'Jackal':
            animal.alive = False
        return


class Jackal(Animal):
    def talk(self):
        if self.alive:
            return 'Woof! Woof!'

    def hunt(self, animal):
        if animal.__class__.__name__ == 'Rabbit':
            animal.alive = False
        return


class Rabbit(Animal):
    def talk(self):
        if self.alive:
            return 'Sniff Sniff!'

    def hunt(self, animal):
        if animal.__class__.__name__ == 'Mouse':
            animal.alive = False


class Mouse(Animal):
    def talk(self):
        if self.alive:
            return 'Squeak!'


class Snail(Animal):
    def talk(self):
        if self.alive:
            return 'Squeak'

if __name__ =='__main__':
   test_animal = TestAnimal()
   test_animal.test_talk()
   test_animal.test_hunt()
