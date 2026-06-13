def solution(date1, date2):
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    if y1 == y2:
        if m1 == m2:
            if d1 < d2:
                return 1
            else:
                return 0
        elif m1 < m2:
            return 1
        else:
            return 0
    elif y1 < y2:
        return 1
    else: return 0