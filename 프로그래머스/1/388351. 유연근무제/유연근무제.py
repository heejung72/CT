def solution(schedules, timelogs, startday):

# 출근 희망 시간 + 10분
# 토, 일 영향 x
# 시 * 100 + 분
  
    answer = 0
    for schedule, timelog in zip(schedules, timelogs):
        schedule = (schedule // 100) * 60 + schedule % 100
        pass_point = 0 # 사람마다
        for r, time in enumerate(timelog):
            r += startday
            if (r % 7 != 6 and r% 7 != 0):
                time = (time // 100) * 60 + time % 100
                
                if time - schedule > 10:
                    pass_point = -1
                
        if pass_point == 0:
            answer += 1
    
    return answer

