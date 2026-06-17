import math

def solution(a, b):
    divisor = math.gcd(a,b)
    rem = b // divisor
    
    while rem % 2 == 0:
        rem /= 2
    
    while rem % 5 == 0:
        rem /= 5
    
    if rem == 1:
        return 1
    else:
        return 2