def solution(arr, delete_list):
    arr_org = {j: i for i, j in enumerate(arr)}
    arr_del = set(arr) - set(delete_list)
    answer = {}
    for num in arr_del:
        answer[num] = arr_org[num]
    answer = sorted(answer, key = answer.get)
    return answer