def solution(hp):
    # 장군 5, 병정 3, 일 1 > dict
    ants = 0
    for i in [5, 3, 1]:
        ants += hp // i
        hp = hp % i
    return ants