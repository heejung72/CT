class Human():
    '''인간'''
    def __init__(self, name, weight):
        '''초기화'''
        print("init 실행")
        self.name = name
        self.weight = weight
        print("이름 {} 몸무게 {}".format(name, weight))

    def __str__(self):
        '''문자열화 함수'''
        return "{} ({}kg)".format(self.name, self.weight)
        # print(person)하면 이거 출력

    def create_human (name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person
    def eat(self):
        self.weight += 0.1
        print("{}".format(self.weight))

    def walk(self):
        self.weight -=0.1
        print("{}".format(self.weight))

# person = Human()
# person.name = '철수'
# person.weight = 60.5

person = Human("희",0.6)
print(person.name)
print(person.weight)

person.eat()
