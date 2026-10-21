class Human():
    '''인간'''

# person = Human()
# person.name = '철수'
# person.weight = 60.5

def create_human (name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

Human.create = create_human
person = Human.create('철수', 60.5)

def eat(person):
    person.weight += 0.1

def walk(person):
    person.weight -=0.1

Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()

