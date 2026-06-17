def solution(my_string):
    my_string = my_string.lower()
    alph = list(my_string)
    alph.sort()
    return "".join(alph)