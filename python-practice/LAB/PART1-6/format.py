number = 20
greeting = 'hello'
place = 'string world'
welcome = 'welcome'

print(number, '먼 손님', greeting, '.', place,
      '에 오신 것을', welcome, '!')

base = '{}번 손님, {}. {}에 오신 것을 {} !'
new_way = base.format(number, greeting
                      ,place, welcome)

print(base)
print(new_way)

# format은 {}에 뭔가를 넘어줌.

mine = "가위"
yours = "바위"
result = "졌다"

print("나는 {}, 너는 {}. 그래서 {}".format(mine, yours, result))
