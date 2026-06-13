def solution(arr):
    n = 0
    l = len(arr)
    while True:
        if 2**n < l and 2**(n+1) > l:
            n += 1
            break
        elif 2**n == l:
            break
        n+=1
    arr += [0] * (2**n-len(arr))
    return arr