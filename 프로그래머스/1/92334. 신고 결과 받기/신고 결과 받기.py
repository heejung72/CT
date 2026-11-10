def solution(id_list, report, k):

    # 1. 딕셔너리 만들어서 신고한 대상을 set으로 (중복 방지) 저장한다. 
    reported_dict = { user : set() for user in id_list }
    
    for i in report:
        user, target = i.split()
        reported_dict[user].add(target)
    
    # 2. 유저별 신고 count
    reported = { user : 0 for user in id_list }
    for user in id_list:
        for target in reported_dict[user]:
            reported[target] += 1
    
    # 3. k보다 많은지
    answer = []
    
    for user in id_list:
        count = 0

        for target in reported_dict[user]:
            if reported[target] >= k:
                count += 1

        answer.append(count)

    return answer
