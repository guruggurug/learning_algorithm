def solution(my_string, n):
    my_string_list = list(my_string)
    for i in range(len(my_string_list)):
        my_string_list[i] = my_string_list[i]*n
    return "".join(my_string_list)