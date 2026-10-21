def solution(s):

    if (s[:1] == '-'):
        number = int(s[1:]) * (-1)
        
    if (s[:1] == '+'):
        number = int(s[1:])
    return int(s[:])