def solution(x):
    original = x  
    digit_sum = 0

    for i in range(len(str(x))):
        digit_sum += x % 10
        x //= 10

    return original % digit_sum == 0