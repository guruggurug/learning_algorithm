def solution(n):
    prime_n = [2,3,5,7,11,13,17,19,23]
    result = []
    for pm in prime_n:
        for i in range(pm*2,n+1,pm):
            if i not in result:
                result.append(i)
    return len(result)