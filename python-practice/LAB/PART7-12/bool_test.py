# value = input("input") or '아무것도 못받았어'
# print('입력받은 값,', value)

# input("input") 이 빈 경우 무조건 or 의 뒷부분이 정답이 된다

if []:
    print("[]은 True입니다.")

if [1, 2, 3]:
    print("[1,2,3]은/는 True입니다.")

if {}:
    print("{}은 True입니다.")

if {'abc': 1}:
    print("{'abc':1}은 True입니다.")

if 0:
    print("0은/는 True입니다.")

if 1:
    print("1은 True입니다.")

a = 1 or 10    # 1의 bool 값은 True입니다.
b = 0 or 10    # 0의 bool 값은 False입니다.

print("a:{}, b:{}".format(a, b)) # 1 # 10
