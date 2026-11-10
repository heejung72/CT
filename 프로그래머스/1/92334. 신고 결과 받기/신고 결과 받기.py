def solution(id_list, report, k):
    # 딕셔너리 만들어서 신고당한 횟수 저장
    # 동일 유저 신고 횟수는 1회 -> set
    
    report_dict = {user : set() for user in id_list}
    for a in report:
        user, target = a.split()
        report_dict[user].add(target)
        
    reported = {user : 0 for user in id_list}

    for user in id_list:
        for target in report_dict[user]:
            reported[target] += 1
    
    # 정지된 target을 신고한 user에게 메일보내기
    answer = []
    for user in id_list:
        count = 0
        for target in report_dict[user]:
            if reported[target] >= k:
                count+=1
        answer.append(count)
        
    return answer