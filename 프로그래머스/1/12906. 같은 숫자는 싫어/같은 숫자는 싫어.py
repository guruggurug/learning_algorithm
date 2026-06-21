from collections import deque

def solution(arr):
    answer = []
    arr = deque(arr)
    
    answer.append(arr.popleft())
    
    # 연속된 숫자인지 판별
    while arr:
        number = arr.popleft()
        if number == answer[-1]:
            pass
        else:
            answer.append(number)
    return answer