def rsp (mine, yours):
    allowed = ['가위','바위']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError

try : rsp('바','보')
except : print("에러 ㅠㅠ")

