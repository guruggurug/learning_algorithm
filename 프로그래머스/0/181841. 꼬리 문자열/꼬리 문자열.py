def solution(str_list, ex):
    return "".join(["" if ex in i else i for i in str_list])