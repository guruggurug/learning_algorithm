import heapq

def solution(A, B):
    # 완전 탐색 느낌으로다가
    
    A.sort()    # 1, 3, 5, 7
    # B.sort()    # 2, 2, 6, 8
    
    heapq.heapify(B)
    
    won = 0
        
    for i in range(len(A)):
        A_member = A[i]
        # for j in range(len(B)):
        #     if B_candidate < B[j]:
        #         # print('B_candidate', B_candidate, '<', 'B[j]', B[j])
        #         # del B[j]
        #         B = B[j+1:]
        #         won += 1
        #         # print('B updated', B, 'won', won)
        #         break
        # else:
        #     break
        
        while B:
            B_popped = B[0]
            if A_member < B_popped:
                heapq.heappop(B)
                won += 1
                break
            else:
                B_popped = heapq.heappop(B)
            
    return won