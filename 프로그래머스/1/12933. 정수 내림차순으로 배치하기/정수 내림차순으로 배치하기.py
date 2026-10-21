def solution(n):
    length = len(str(n))
    digits = []
    
    for i in range(length):
        digit = (n // (10**i)) % 10
        digits.append(digit)
        
    digits.sort(reverse=True)
    
    answer = 0
    for i in range(len(digits)):
        answer += digits[i] * (10 ** (length - i-1))
    
    return answer