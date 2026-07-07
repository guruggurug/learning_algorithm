def solution(array):
    array = list(map(str, array))
    array_str = "".join(array)
    return array_str.count("7")