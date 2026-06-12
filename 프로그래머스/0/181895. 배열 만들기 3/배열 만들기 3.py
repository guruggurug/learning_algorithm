def solution(arr, intervals):
    a1,a2 = intervals
    return arr[a1[0]:a1[1]+1] + arr[a2[0]:a2[1]+1]