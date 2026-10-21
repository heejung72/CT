wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}
print(wintable['가위'])

def rsp (mine, yours):
    if mine == yours:
        print("비김")
    elif wintable[mine] == yours:
        print("win")
    else:
        print("lose")

rsp('가위', '보')
rsp('가위','바위')
