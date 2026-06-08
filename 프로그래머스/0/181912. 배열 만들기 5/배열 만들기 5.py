def solution(intStrs, k, s, l):
    ret = []
    for strs in intStrs:
        strs_to_int = int(strs[s:s+l])
        if strs_to_int > k:
            ret.append(strs_to_int)
    return ret