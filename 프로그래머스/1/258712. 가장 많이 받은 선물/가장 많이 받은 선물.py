
def solution(friends, gifts):
    # 선물 주고받은 횟수 저장
    gift_count = {}

    for me in friends:
        gift_count[me] = {}

        for other in friends:
            if me != other:
                gift_count[me][other] = 0

    for gift in gifts:
        giver, receiver = gift.split()
        gift_count[giver][receiver] += 1

    # 선물 지수 계산
    present_point = {}

    for friend in friends:
        # 준 선물 수
        total = sum(gift_count[friend].values())

        # 받은 선물 수
        for other in friends:
            if other != friend:
                total -= gift_count[other][friend]

        present_point[friend] = total

    # 다음 달 선물 개수 계산
    next_month_present = {}

    for friend in friends:
        next_month_present[friend] = 0

    # 같은 친구 쌍을 두 번 비교하지 않도록 인덱스 사용
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            friend = friends[i]
            other = friends[j]

            give = gift_count[friend][other]
            receive = gift_count[other][friend]

            if give < receive:
                # 선물을 많이 준 other가 다음 달에 받음
                next_month_present[other] += 1

            elif give > receive:
                # 물을 많이 준 friend가 다음 달에 받음
                next_month_present[friend] += 1

            else:
                # 주고받은 횟수가 같거나 기록이 없는 경우
                if present_point[friend] > present_point[other]:
                    next_month_present[friend] += 1

                elif present_point[friend] < present_point[other]:
                    next_month_present[other] += 1

                # 선물 지수까지 같으면 아무도 받지 않음

    return max(next_month_present.values())
