def solution(arr):
    #[[572, 22, 37],
    #[287, 726, 384],
    #[85, 137, 292],
    #[487, 13, 876]]
    
    num = len(arr) - len(arr[0])
    
    if num < 0:
        for _ in range(-num):
            arr.append([0]*len(arr[0]))
    elif num > 0:
        for i in range(len(arr)):
                   arr[i] += [0]*num
    return arr