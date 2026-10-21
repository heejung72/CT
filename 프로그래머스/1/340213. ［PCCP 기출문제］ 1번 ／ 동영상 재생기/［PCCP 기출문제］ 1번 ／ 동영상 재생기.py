def solution(video_len, pos, op_start, op_end, commands):
    # prev -10
    # next +10
    # op_start<=현재 <=op_end -> op_end
    
    video_len = video_len.split(":")
    video_second = int(video_len[0]) * 60 + int(video_len[1])
    pos = pos.split(":")
    pos_second = int(pos[0]) * 60 + int(pos[1])
    op_start = op_start.split(":")
    op_start_second = int(op_start[0]) * 60 + int(op_start[1])
    op_end = op_end.split(":")
    op_end_second = int(op_end[0]) * 60 + int(op_end[1])
    
    for command in commands:
        if (op_start_second <= pos_second <= op_end_second):
            pos_second = op_end_second
            
        if (command == "prev"):
            if (pos_second < 10 ):
                pos_second = 0
            else : 
                pos_second -= 10
        
        elif (command == "next"):
            if (pos_second > video_second-10):
                pos_second = video_second
            else :
                pos_second += 10
            
        if (op_start_second <= pos_second <= op_end_second):
            pos_second = op_end_second
     
    minute = pos_second//60
    second = pos_second%60
    return f"{minute:02d}:{second:02d}"
 