def solution(my_string, indices):
    my_list = list(my_string)
    for i in indices:
        my_list[i] = ""    

    return "".join(my_list)