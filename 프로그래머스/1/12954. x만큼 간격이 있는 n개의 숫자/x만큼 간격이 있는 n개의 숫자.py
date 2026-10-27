def solution(x, n):
    list = [] 
    count = 0
    for i in range(n):
        count += 1
        list.append(x * (i+1))
        if (n == count):
            return list
        