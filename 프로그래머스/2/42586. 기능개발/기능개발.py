import math
from collections import deque

def count(days_que):
    count = 1
    result = []
    today = 1
    while days_que:
        today_max = max(days_que.popleft(), today)
        if days_que:
            nday = days_que[0]
            if today_max >= nday:
                count += 1
            else:
                result.append(count)
                count = 1
            today = today_max
        else:
            result.append(count)
    return result

def solution(progresses, speeds):
    days = []
    pro_speed = list(zip(progresses, speeds))
    for i, j in pro_speed:
        day = (99-i)//j+1
        # day = math.ceil((100-i)//j)
        # math.floor
        days.append(day)
    days_que = deque(days)
    return count(days_que)