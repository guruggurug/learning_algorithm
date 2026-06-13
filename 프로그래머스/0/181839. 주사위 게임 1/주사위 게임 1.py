def solution(a, b):
    ar, br = a%2, b%2
    # if ar or br:
    #     if ar and br:
    #         return a**2 + b**2
    #     return 2*(a+b)
    if ar and br:
        return a**2 + b**2
    elif ar or br:
        return 2*(a+b)
    else:
        return abs(a-b)