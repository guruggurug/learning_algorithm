import heapq

def solution(jobs):
    jobs_priority = []
    count = 0
    
    in_line = []
    
    t = 0
    worked_t = []
    
    
    # 요청 시각 기준으로 정렬
    
    
    # 작업에 들어갈 때는 아래 우선순위를 기준으로,
    # 1. 소요 시간이 짧은 것
    # 2. 요청 시각이 빠른 것
    # 3. 작업의 번호가 작은 것
    
    # jobs의 [요청 시각, 소요 시간] 데이터를
    # [소요 시간, 요청 시각, 작업 번호] 형태로 저장
    for i, j in enumerate(jobs):
        jobs_priority += [[j[1], j[0], i]]

    
    while count < len(jobs):
        # print('jobs_priority: ', jobs_priority)        
        # print('in_line: ', in_line)
        
        
        for i in range(len(jobs_priority)):
            if jobs_priority[i] != 'pushed' and t >= jobs_priority[i][1]:
                heapq.heappush(in_line, jobs_priority[i])
                jobs_priority[i] = 'pushed'
        
        
        # 대기 큐가 비어있지 않을 때 작업 하나를 완료시키기
        # [소요 시간, 요청 시각, 작업 번호] 데이터에서 t += 소요 시간
        if in_line:
            task = heapq.heappop(in_line)
            # print('작업 중 task: ', task)
            t += task[0]
            worked_t.append(t-task[1])
            count += 1
            

            # print('대기 작업 하나 완료', 't: ', t, 'worked_t: ', worked_t, 'count: ', count)
    

        # 대기 큐가 비어있을 때
        # 작업 대기 큐에 push + 현재 시간 업데이트
        else:
            t += 1
                    
    
    # worked_t 데이터 평균 return하기
    return sum(worked_t)//len(worked_t)