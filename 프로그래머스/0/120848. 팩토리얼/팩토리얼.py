def addfactorial(num, list_):
    list_.append(list_[-1]*num)
    return list_

def solution(n):
    num = 2
    list_ = [1]
    while True:
        list_ = addfactorial(num, list_)
        if list_[-1] > n:
            return num-1
        if list_[-1] == n:
            return num
        num += 1