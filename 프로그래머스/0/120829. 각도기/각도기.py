def solution(angle):
    # dict = {range(1,90):1, range(91,180):3, 90: 2, 180: 4}
    # return dict[angle]
    if angle == 180:
        return 4
    elif angle > 90:
        return 3
    elif angle == 90:
        return 2
    elif angle < 90:
        return 1