class Animal():
    def __init__(self,name):
        self.name = name
    def walk(self):
        print("walk")
    def eat(self):
        print("eat")
    def greet(self):
        print("{}가 인사한다".format(self.name))

class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand=hand
    def wave(self):
        print("wave hand And I said")
    def greet(self):
        self.wave()
        super().greet()

class Dog(Animal):
    def wag(self):
        print("wag tail")
    def greet(self):
        self.wag()

class Cow(Animal):
    '''소 '''
person = Human("사람", "오른손")
person.greet()
