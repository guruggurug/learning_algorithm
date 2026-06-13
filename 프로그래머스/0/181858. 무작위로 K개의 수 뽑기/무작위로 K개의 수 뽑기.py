def solution(arr, k):
    # set로 만들면 list의 index에 매핑되어 있는 게 사라지니까 오류 발생
    # arrtoset = list(set(arr))
    # print(arrtoset)
    # result = [-1]*k
    # for i in range(min(len(arrtoset),k)):
    #     result[i] = arrtoset[i]
    # return result
    result = [-1]*k
    i = 0
    for j in range(len(arr)):
        if arr[j] not in result:
            result[i] = arr[j]
            i += 1
        if i == k:
            break
    return result