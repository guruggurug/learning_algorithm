def solution(a, b, c, d):
    answer = 1
    ls = [a,b,c,d]
    ls.sort()
    result = {a,b,c,d}
    #pppp
    if len(result) == 1:
        answer = 1111 * a
    #pppq
    elif len(result) == 2:
        p = ls[1]
        q = ls[2]  #1113 #1333
        if p == q:
            if ls[0] == ls[1]:
                p = ls[0]
                q = ls[-1]
                answer = (10*p+q)**2
            else:
                p = ls[-1]
                q = ls[0]
                answer = (10*p+q)**2
        else:
            answer = (p+q)*((p-q)**2)**0.5
    elif len(result) == 3:
        duplicate = []
        for i in (0,1,2):
            if ls[i] == ls[i+1]:
                ls[i] = 1
                ls[i+1] = 1
                break
        answer = ls[0] * ls[1] * ls[2] * ls[3]
    else:
        answer = min(result)
        
    return answer