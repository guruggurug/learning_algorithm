def solution(num, total):
    pivot = total // num
    if num % 2:
        return [i for i in range(pivot-num//2,pivot+num//2+1)]
    else:
        return [i for i in range(pivot-num//2+1, pivot+num//2+1)]