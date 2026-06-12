def solution(arr):
    if 2 in arr:
        l = arr.index(2)
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 2:
                r = i
                break
        return arr[l:r+1]
    else:
        return [-1]