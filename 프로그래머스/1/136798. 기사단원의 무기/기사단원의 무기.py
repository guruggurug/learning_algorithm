def divisor(number):
    count = 0
    root = int(number**0.5)
    for i in range(1,root+1):
        if number % i == 0:
            count += 2
    if root**2 == number:
        count -= 1
    return count

def solution(number, limit, power):
    result = []
    # number = [i for i in range(1,number+1)]
    num = []
    for i in range(1,number+1):
        num.append(i)
    while num:
        knight = num.pop()
        knight_power = divisor(knight)
        if knight_power > limit:
            knight_power = power
        result.append(knight_power)
    return sum(result)