def solution(emergency):
    result = [0]*len(emergency)
    emergency_index = [(j,i) for i,j in enumerate(emergency)]
    emergency_index.sort()
    emergency_index.reverse()
    priority = 1
    for i in emergency_index:
        result[i[1]] = priority
        priority += 1
    return result