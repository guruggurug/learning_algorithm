def solution(my_string, m, c):
    # ihrhbakrfpndopljhygc
    
    # ihrh  1
    # bakr  5
    # fpnd  9
    # oplj  13
    # hygc  17
    
    result = ""
    result += my_string[c-1::m]
    
    return result