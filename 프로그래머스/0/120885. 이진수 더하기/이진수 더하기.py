def solution(bin1, bin2):
    # int()
    int1 = int(bin1, 2)
    int2 = int(bin2, 2)
    answer = int1 + int2
    return bin(answer)[2:]