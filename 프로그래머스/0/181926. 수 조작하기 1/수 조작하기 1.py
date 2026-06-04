def solution(n, control):
    w_count = control.count("w")
    s_count = control.count("s")
    a_count = control.count("a")
    d_count = control.count("d")
    # print(w_count, s_count, a_count, d_count)
    n += w_count - s_count + 10*d_count - 10*a_count
    return n
    