def solution(my_string, letter):
    #아이디어 1: 하나씩 보면서 제거
    my_string_updated = ""
    for i in range(len(my_string)):
        if my_string[i] != letter:
            my_string_updated += my_string[i]
    return my_string_updated