def solution(dot):
    x = dot[0]
    y = dot[1]
    dict = {(x<0,y<0):3, (x>0,y>0):1, (x<0,y>0):2, (x>0,y<0):4}
    return dict[(True,True)]