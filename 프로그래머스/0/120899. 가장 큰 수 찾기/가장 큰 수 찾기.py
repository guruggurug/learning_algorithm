def solution(array):
    result = []
    num = max(array)
    result += [num, array.index(num)]
    return result