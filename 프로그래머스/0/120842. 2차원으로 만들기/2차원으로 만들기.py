def solution(num_list, n):
    result = []
    for i in range(len(num_list)//n):
        result.append(list(num_list[n*i:n*(i+1)]))
    return result