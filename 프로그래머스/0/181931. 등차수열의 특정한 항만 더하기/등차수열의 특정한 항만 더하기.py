def solution(a, d, included):
    answer = 0
    for idx in range(len(included)):
        txt = included[idx]
        if txt:
            included[idx] = a + d * idx
        else:
            included[idx] = 0
    answer = sum(included)
    return answer