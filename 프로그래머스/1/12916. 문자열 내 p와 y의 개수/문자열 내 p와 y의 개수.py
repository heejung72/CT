def solution(s):
    s= s.lower()
    countp = 0
    county = 0
    
    for i in s:
        if (i == "p"):
            countp +=1
        if (i == "y"):
            county +=1
        
    if (countp == county):
        return True
    return False