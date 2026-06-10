def solution(my_string):
    answer = [0] * 52
    
    for l in my_string:
        l_ord = ord(l)
        if l_ord <= 90:
            answer[l_ord-65] += 1
        else:
            answer[l_ord-97+26] += 1
        
    return answer