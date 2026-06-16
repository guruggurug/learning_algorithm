def solution(rsp):
    winning = {'2': '0', '0': '5', '5': '2'}
    result = ""
    for t in rsp:
        result += winning[t]
    return result