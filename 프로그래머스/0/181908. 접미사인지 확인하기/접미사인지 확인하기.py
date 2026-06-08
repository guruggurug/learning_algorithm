def solution(my_string, is_suffix):
    # 아이디어 1
    my_suffix = list(my_string[i:] for i in range(len(my_string)))
    if is_suffix in my_suffix:
        return 1
    else:
        return 0