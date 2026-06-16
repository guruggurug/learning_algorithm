def solution(order):
    digits = list(str(order))
    return digits.count('3') + digits.count('6') + digits.count('9')