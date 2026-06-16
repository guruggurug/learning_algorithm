def solution(n):
    # 약수 구해주는 메서드 있을 것 같음!
    answer = [1, n]
    # if type(n**0.5) == type(int):
    #     answer.append(n**0.5)
    for i in range(2,int(n**0.5)+1): # float여도 range에 들어갈 수 있나? > 안 됨
        if n % i == 0:
            answer += [i, n//i]
            print(answer)
    return len(set(answer))