def solution(arr, flag):
    # true면 arr[i] * 2 번만큼
    # false면 arr[i] 만큼 제거
    X = []
    for i, j in enumerate(flag):
        if j:
            X += [arr[i]] * (arr[i]*2)
        else:
            if not X:
                continue
            else:
                X = X[:-arr[i]]
    return X