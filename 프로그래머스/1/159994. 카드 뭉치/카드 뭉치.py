from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    i = 0
    for i in range(len(goal)):
        flag = 0
        for c in [cards1, cards2]:
            if len(c) > 0:
                if goal[i] == c[0]:
                    c.popleft()
                    flag = 1
            else:
                pass
        if flag == 0:
            return "No"
    
    return "Yes"
    
    # for i in range(len(goal)):
    #     # if goal[i] in cards1: 완전 틀린 논리
    #     if goal[i] == cards1[0]:
    #         cards1.popleft()
    #     # elif goal[i] in cards2: 완전 틀린 논리
    #     elif goal[i] == cards2[0]:
    #         cards2.popleft()
    #     else:
    #         return "No"
    # return "Yes"

    # 반례?!
    # if len(cards1) == 0 and len(cards2) == 0:
    #     return "Yes"
    # else:
    #     return "No"