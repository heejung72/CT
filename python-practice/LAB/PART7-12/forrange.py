for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(10): # (0~9)
    print(i)

names = ['철수', '영희', '바둑이']

for i in range(len(names)):
    name = names[i]
    print('{}번 {}'.format(i+ 1,name))

for i, name in enumerate(names):
    print('{}번 {}'.format(i+1, name))

# enumerate 짝
for i in range(11172):
    print(chr(44402 + i))
