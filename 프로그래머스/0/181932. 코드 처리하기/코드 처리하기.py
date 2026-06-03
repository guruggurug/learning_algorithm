# 1차 채점 결과: 실패 (정확성 84.6/100)
# mode 전환 테스트에 집중하느라 EMPTY 출력 조건을 고려하지 않았다!


def solution(code):
    ret = ''
    mode = 0
    # 1은 mode를 전환시키는 flag
    # mode가 0이면 짝수 index 문자 +
    # mode가 1이면 홀수 index 문자 +
    
    # for문을 돌리지만 시간 복잡도를 줄일 수는 없을까?
    
    for idx in range(len(code)):
        # flag 감지
        if code[idx] == "1":
            # mode가 0 또는 1이니까 not mode로 전환시킬 수 있을까?
            # 위의 가설 테스트
            # mode = not mode
            # 테스트 결과: 전환 안 됨!
            
            # 조건문 쓰면 간단하게 해결 가능
            # 다른 방법은 없는 걸까?
            
            # 자료형을 변환해야 전환이 될까?
            mode = int(not bool(mode))
            # 테스트 결과: 전환 안 됨!
            
            # 다시 보니 1의 자료형이 int가 아니라.... str이었다....
            # if code[idx] == 1 -> if code[idx] == "1"로 수정
            # 테스트 결과: 두 코드 모두 작동함!
            
        # flag가 아닌 문자열
        else:
            # mode가 1일 때 > 홀수 index str 추가
            if mode:
                # 홀수 index 판별
                if idx % 2:
                    ret += code[idx]
            # mode가 0일 때
            else:
                # 짝수 index 판별
                if not idx % 2:
                    ret += code[idx]
        # ret 확인용, mode 확인용
        # print(f'mode: {mode}, idx: {idx}, ret: {ret}')
    # ret가 빈 문자열일 때
    if not ret:
        ret = 'EMPTY'
    return ret