def solution(my_string, num1, num2):
    str1 = my_string[num1]
    str2 = my_string[num2]
    # str은 immutable이니까
    return my_string[:num1] + str2 + my_string[num1+1:num2] + str1 + my_string[num2+1:]