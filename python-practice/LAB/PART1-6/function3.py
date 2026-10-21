a = 1
b = 2
c = -8

r1 = (-b + (b ** 2 - 4*a*c) ** 0.5) / 2*a
r2 = (-b - (b ** 2 - 4*a*c) ** 0.5) / 2*a

print('해는 {} 또는 {}'.format(r1, r2))

a = 2
b = 4
c = 3

r1 = (-b + (b ** 2 - 4*a*c) ** 0.5) / 2*a
r2 = (-b - (b ** 2 - 4*a*c) ** 0.5) / 2*a

print('해는 {} 또는 {}'.format(r1, r2))

# 불편
# 함수만들자
def print_sqrt(a, b, c) :
    r1 = (-b + (b ** 2 - 4*a*c) ** 0.5) / 2*a
    r2 = (-b - (b ** 2 - 4*a*c) ** 0.5) / 2*a

    print('해는 {} 또는 {}'.format(r1, r2))

a = 2
b = 4
c = 3


x = 4
y = 4
z = 3

print_sqrt(x, y, z)

def print_round(number):
    rounded = round(number)
    print(rounded)

print_round(4.6)

