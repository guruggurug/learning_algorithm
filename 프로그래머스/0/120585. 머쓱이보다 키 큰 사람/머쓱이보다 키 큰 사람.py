def solution(array, height):
    array.append(height)
    array.sort()
    array.reverse()
    rank = array.index(height)
    return rank