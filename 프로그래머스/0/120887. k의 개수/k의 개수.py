def solution(i, j, k):
    numbers = []
    for n in range(i,j+1):
        numbers.append(str(n))
    numbers_str = "".join(numbers)
    return numbers_str.count(str(k))