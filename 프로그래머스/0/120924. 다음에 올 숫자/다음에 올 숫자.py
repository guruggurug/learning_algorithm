def solution(common):
    num1 = common[-3]
    num2 = common[-2]
    num3 = common[-1]
    
    if num3-num2 == num2-num1:
        return num3+num3-num2
    else:
        return num3*(num3//num2)