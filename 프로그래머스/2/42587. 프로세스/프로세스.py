from collections import deque

def solution(priorities, location):
    p_que = deque([(i,j) for i, j in enumerate(priorities)])
    count = 0
    while p_que:
        priority = max(j for i,j in p_que)
        process = p_que.popleft()
        # priority = max([p[1] for p in process])
        if process[1] < priority:
            p_que.append(process)
        else:
            count += 1
            if process[0] == location:
                return count
    return count