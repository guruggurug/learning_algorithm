def solution(numbers):
    can = []
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    if len(numbers) == 3:
        return max(numbers[0]*numbers[1], numbers[1]*numbers[2])
    for _ in range(2):
        pos = max(numbers)
        neg = min(numbers)
        numbers.remove(pos)
        numbers.remove(neg)
        can += [pos,neg]
    can.sort()
    return max(can[0]*can[1], can[2]*can[3])