import math as m

def solution(numer1, denom1, numer2, denom2):

    #denom1이랑 denom2랑 최소공배수 구하고 싶다.
    lcm12 = m.lcm(denom1, denom2)
    numer3= int(numer1 * lcm12 / denom1 + numer2 * lcm12 / denom2)
    gcd12 = m.gcd(numer3, lcm12)
    answer = [numer3 / gcd12, lcm12 / gcd12]
    return answer