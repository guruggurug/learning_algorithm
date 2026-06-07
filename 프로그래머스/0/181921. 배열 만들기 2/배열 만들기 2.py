def solution(l,r):
    # 숫자 하나씩 떼서 보기?
    l_list = list(map(int,str(l)))
    r_list = list(map(int,str(r)))
    
    l_digit = len(str(l))
    r_digit = len(str(r))
    
    # l보다 크지만 가장 작은 이진수 변환
    if l > int("5"*l_digit):    # 56부터 100으로
        l_bin = "1"+"0"*l_digit
    elif l_list[0] < 5:    # 40이면 10으로
        l_bin = "1"+"0"*(l_digit-1)
    elif l_list[0] == 5:
        l_list[0] = 1
        for l in range(1, l_digit):
            if l_list[l] > 5:
                l_list[l:] = [0] * (l_digit-l)
                if l_list[l-1] == 1:
                    l_list[l-2] = 1
                    l_list[l-1] = 0
                else:
                    l_list[l-1] = 1
                break
            elif l_list[l] == 0:
                l_list[l] = 0
            elif l_list[l] <= 5 and l_list[l] != 0:
                l_list[l] = 1
        l_bin = "".join(map(str,l_list))
    # r의 구간
    if r < int("5"+"0"*(r_digit-1)):    # 49부터 5로
        r_bin = "1"*(r_digit-1)
    elif r_list[0] > 5:    # 600이면 555로
        r_bin = "1"*r_digit
    elif r_list[0] == 5:    # 5__이면 판단해야 함
        r_list[0] = 1
        for r in range(1, r_digit):
            if r_list[r] >= 5:
                r_list[r] = 1
            elif r_list[r] < 5 and r_list[r] > 0:
                r_list[r] = 0
                r_list[r+1:] = [1]*(r_digit-r-1)
                break
            elif r_list[r] == 0:
                r_list[r] = 0
        r_bin = "".join(map(str,r_list))

    l_ten = int(l_bin,2)
    r_ten = int(r_bin,2)

    result_bin = []
    if l_ten <= r_ten:
        for i in range(l_ten, r_ten+1):
            result_bin.append(bin(i)[2:])

    result_ten = []    
    for i in result_bin:
        result_ten.append(int(i)*5)

    if not result_ten:
        return [-1]    
    else:
        return result_ten