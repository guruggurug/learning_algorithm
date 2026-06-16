def solution(n):
    result = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            result += [i, n//i]
            if i == n//i:
                # del result[-1]
                result.pop()
    result.sort()
    return result