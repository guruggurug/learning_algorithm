def solution(n):
    i = n**0.5
    if int(i)**2 == n:
        return 1
    else:
        return 2