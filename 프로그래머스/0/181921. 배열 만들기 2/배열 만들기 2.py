def solution(l,r):
    l_digit = len(str(l))
    r_digit = len(str(r))
        
    result_bin = []
    # l_digit과 r_digit 기준으로 이진수 생성하기
    # l이 두 자리 수면 10부터, 세 자리 수면 100부터
    # r이 두 자리 수면 11(100에서 하나 전)까지, 세 자리 수면 111(1000에서 하나 전)까지
    for i in range(2**(l_digit-1), 2**r_digit):
        result_bin.append(bin(i)[2:])
    
    result_ten = []
    for i in result_bin:
        i = int(i)*5
        if i >= l and i <= r:
            result_ten.append(i)
    
    if not result_ten:
        return [-1]
    else:
        return result_ten