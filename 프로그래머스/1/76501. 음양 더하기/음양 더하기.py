def solution(absolutes, signs):
    sum = 0
    for a, s in zip(absolutes, signs):
        if s == True:
            sum += a
        if s == False:
            sum -= a
    return sum