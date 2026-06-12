def solution(n, slicer, num_list):
    # n = 1 [:b]
    # n = 2 [a:]
    # n = 3 [a:b]
    # n = 4 [a:b:c]
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    
    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    else:
        return num_list[a:b+1:c]