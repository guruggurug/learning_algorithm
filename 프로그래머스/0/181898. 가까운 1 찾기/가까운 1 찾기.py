def solution(arr, idx):
    arr = arr[idx:]
    return arr.index(1)+idx if 1 in arr else -1