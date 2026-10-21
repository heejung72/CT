selected = None
while selected not in ['가위', '바위', '보']:
    selected = input ('가위 바위 보 중에서 선택해')

print(selected)


patterns = ['가위', '보', '보']
for i in patterns:
    print(i)


for i in range(len(patterns)):
    print(patterns[i])

i = 0
while i <len(patterns):
    print(patterns[i])
    i = i+1

