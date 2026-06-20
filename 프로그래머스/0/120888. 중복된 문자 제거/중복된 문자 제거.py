def solution(my_string):
    my_list = []
    for i in my_string:
        if i in my_list:
            pass
        else:
            my_list.append(i)
    return "".join(my_list)