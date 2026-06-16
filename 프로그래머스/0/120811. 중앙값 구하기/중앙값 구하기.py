def solution(array):
    array.sort()
    mid = int(len(array) / 2)
    return array[mid] if len(array)%2==1 else (array[mid] + array[mid+1])/2