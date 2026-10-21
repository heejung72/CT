class Human():
    '''사람'''

person1 = Human()
person2 = Human()

# 리스트에서 인스턴스 만들었던 것처럼

a = list()
print(a)
isinstance(a, list)
list1 = [1,2,3,4,5]
list1.append(6)

person1.language = 'Korean'
person2.language = 'English'

print(person1.language)
print(person2.language)

person1.name = 'HEE'
print(person1.name)

def speak(person):
    print("{}이 {}로 말을 한다.".format(person.name, person.language))

Human.speak = speak
person1.speak()
