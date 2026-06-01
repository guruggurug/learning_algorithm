def solution(my_string, overwrite_string, s):
    my_string = str(my_string)
    overwrite_string = str(overwrite_string)
    answer = ''
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    
    return answer