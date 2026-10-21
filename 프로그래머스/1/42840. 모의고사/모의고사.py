def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s1_score = 0
    s2_score = 0
    s3_score = 0
    
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)] :
            s1_score += 1
        if answers[i] == s2[i % len(s2)] :
            s2_score += 1
        if answers[i] == s3[i % len(s3)] :
            s3_score += 1
    
    max_score = max(s1_score, s2_score, s3_score)
    
    result = []

    if s1_score == max_score:
        result.append(1)

    if s2_score == max_score:
        result.append(2)

    if s3_score == max_score:
        result.append(3)

    return result
