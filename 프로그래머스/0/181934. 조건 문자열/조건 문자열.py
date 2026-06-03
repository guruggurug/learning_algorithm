def solution(ineq, eq, n, m):
    #n = m인 경우
    if n == m:
        #eq 판별
        if eq == "=":
            return 1
        else:
            return 0
    #n > m인 경우
    elif n > m:
        #ineq 판별
        if ineq == ">":
            return 1
        else:
            return 0
    #n < m인 경우
    else:
        #ineq 판별
        if ineq == "<":
            return 1
        else:
            return 0