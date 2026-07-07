def solution(s):
    answer = []
    s_set = set(list(s))
    
    for alph in s_set:
        if s.count(alph) == 1:
            answer.append(alph)
    answer.sort()
    return "".join(answer)