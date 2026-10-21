def solution(n, w, num):
    num_row = (num - 1) // w  # if num = 5 면 row 는 1
    num_col = (num - 1) % w # if num = 5 면 col 은 1
    if (num_row % 2 == 1) :
        num_col = w - 1 - num_col
 
    # 마지막 행 번호 
    row = (n-1) // w
    answer = 0
    
    for r in range(num_row, row + 1):
        # 현재 행에 실제로 있는 상자 개수
        count = min(w, n - r * w)

        if r % 2 == 0:
            # 짝수 행: 왼쪽부터 상자가 채워짐
            if num_col < count:
                answer += 1

        else:
            # 홀수 행: 오른쪽부터 상자가 채워짐
            if num_col >= w - count:
                answer += 1

    return answer