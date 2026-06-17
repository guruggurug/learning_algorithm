def solution(num, k):
    digits = list(str(num))
    return digits.index(str(k))+1 if str(k) in digits else -1