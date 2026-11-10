def solution(a, b):
    total = 0
    for a1, b1, in zip(a,b):
        total += a1 * b1
    return total