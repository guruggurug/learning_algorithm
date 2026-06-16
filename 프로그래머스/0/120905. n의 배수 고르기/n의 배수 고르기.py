def solution(n, numlist):
    # end = max(numlist)
    # result = []
    # result += range(n,end,n)
    # return result
    result = []
    for num in numlist:
        if num % n == 0:
            result.append(num)
    return result