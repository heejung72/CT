from UnexpectedRSPValue import *
value = '가'
try:
    if value not in ['가위','바위','보']:
        raise UnexpectedRSPValue
except ValueError:
    print("에러 발생")


def sign_up():
    '''회원가입 함수'''
try :
    sign_up()
except BadUserName:
    print("이름으로 사용할 수 없는 입력입니다")
