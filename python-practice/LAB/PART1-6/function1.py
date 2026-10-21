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
def print_sqrt() :
    r1 = (-b + (b ** 2 - 4*a*c) ** 0.5) / 2*a
    r2 = (-b - (b ** 2 - 4*a*c) ** 0.5) / 2*a

    print('해는 {} 또는 {}'.format(r1, r2))

a = 2
b = 4
c = 3

print_sqrt()
