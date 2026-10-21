from math import lcm
def solution(signals):
    cycles = [g+y+r for g, y, r in signals]
    
    # lcm 최소공배수 gcd 최대공약수
    limit = lcm (*cycles)
    
    for i in range(1, limit +1):
        all_yellow = True
        
        for g, y, r in signals:
            # 0부터 시작
            pos = (i-1) %(g+y+r)
            # 신호가 하나라도 노란불이 아니면 
            if not (g <= pos < g+y):
                all_yellow = False 
                break
        
        if all_yellow:
            # 현재 시각 i 반환
            return i
        
    return -1