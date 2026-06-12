def solution(arr, queries):
    temp = [0] * len(arr)
    for query in queries:
        s, e = query
        for i in range(s,e+1):
            temp[i] += 1
    temp = zip(arr, temp)
    return [i+j for i, j in temp]