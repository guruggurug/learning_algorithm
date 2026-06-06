def solution(number):
    # if number != "0":
    #     number = number.split()
    #     return sum(map(int,number))
    # else:
    #     return 0
    #런타임 에러
    #.split()이 한 일은 없기 때문
    if number != "0":
        number = list(map(int,number))
        return sum(number)%9
    else:
        return 0