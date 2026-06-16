def solution(n):
    answer = 0
    n = str(n)
    for num in n:
        num = int(num)
        answer += num
    return answer