def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, " ")
    my_string = my_string.strip(" ")
    my_string = my_string.split(" ")
    my_number = []
    for n in my_string:
        if n.isdigit():
            my_number.append(int(n))
    return sum(my_number)