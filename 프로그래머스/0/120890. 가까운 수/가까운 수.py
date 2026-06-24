def solution(array, n):
    array_sorted = sorted(array)
    for i in range(len(array_sorted)):
        if array_sorted[i] < n:
            pass
        else:
            point = i
            break
        point = i
    left = n - array_sorted[point-1]
    right = array_sorted[point] - n
    return array_sorted[point-1] if left <= right else array_sorted[point]