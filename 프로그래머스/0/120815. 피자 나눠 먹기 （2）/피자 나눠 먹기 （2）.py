def solution(n):
    # 완전 탐색
    i = 1
    while True:
        if (6*i) % n == 0:
            return i
        else:
            i += 1