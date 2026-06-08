ong = ['aya', 'ye', 'woo', 'ma']

# is_ong 함수 정의
def is_ong(babble):
    if babble == "":
        return ""
    l = len(babble)
    if l == 1:
        return 1
    else:
        if babble[:2] in ong:
            babble = is_ong(babble[2:])
            return babble
        elif babble[:3] in ong:
            babble = is_ong(babble[3:])
            return babble
        else:
            return 1
    

def solution(babbling):
    res = 0
    for babble in babbling:
        # if not is_ong(babble):    None이나 ""이면 0으로 인식하나 봄
        babble = is_ong(babble)
        if babble == "":
            res += 1
    return res