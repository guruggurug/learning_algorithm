def solution(numbers, n):
    temp = 0
    for num in numbers:
        temp += num
        if temp > n:
            return temp