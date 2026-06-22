from collections import deque

def solution(priorities, location):
    p_que = deque([(i,j) for i, j in enumerate(priorities)])
    # [2,1,3,2] -> [(0,2), (1,1), (2,3), (3,2)]
    
    count = 0    # count는 프로세스가 실행되면 +1
    
    while p_que:    # p_que가 비어있지 않는 동안
        
        # [2,1,3,2] 중 최대값을 priority로 저장
        # 첫 번째 실행에서 priority = 3
        priority = max(j for i,j in p_que)
        
        # p_que에서 (0,2) 추출
        # process = (0,2)
        process = p_que.popleft()
        
        if process[1] < priority:
            p_que.append(process)    # 우선순위보다 뒤에 있으므로 enqueue
        else:
            count += 1    # 해당 프로세스를 실행하므로 +1
            if process[0] == location:    # (0,2)에서 0이 location과 같다면 target process가 실행된 순간
                return count