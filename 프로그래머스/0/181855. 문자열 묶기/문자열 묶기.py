def solution(strArr):
    # count = list(map(len,strArr))
    # count.sort()
    # print(count)
    dict = {}
    for str in strArr:
        if len(str) in dict.keys():
            temp = dict[len(str)]
            dict[len(str)] = temp + 1
        else:
            dict[len(str)] = 1
    return max(dict.values())