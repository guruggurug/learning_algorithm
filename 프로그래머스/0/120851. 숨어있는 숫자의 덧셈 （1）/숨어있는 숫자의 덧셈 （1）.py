def solution(my_string):
    num = 0
    for i in my_string:
        if i.isdigit():
            num += int(i)
    return num