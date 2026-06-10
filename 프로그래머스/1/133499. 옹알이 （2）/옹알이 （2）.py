# is_ong 함수 정의
def is_ong(babble, before=''):
    ong = ['aya', 'ye', 'woo', 'ma']

    if babble == "":
        return True
    l = len(babble)
    if l == 1:
        return False
    else:
        if babble[:2] in ong:
            if babble[:2] == before:
                return False
            else:
                return is_ong(babble[2:], babble[:2])
        elif babble[:3] in ong:
            if babble [:3] == before:
                return False
            return is_ong(babble[3:], babble[:3])
        else:
            return False
    

def solution(babbling):
    res = 0
    for babble in babbling:
        if is_ong(babble):
            res += 1
    return res