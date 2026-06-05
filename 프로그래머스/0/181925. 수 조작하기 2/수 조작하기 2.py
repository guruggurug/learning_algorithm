def solution(numLog):
    action = 0
    answer = []
    # dict = {1: 'w', -1: 's', 10:'d', -10: 'a'}
    # 역시나 key값은 int일 수 없다
    # dict = {'w': 1, 's':-1, 'd':10, 'a':-10}
    # 위 구조로는 value 값으로 key 값을 찾아야 하는 상황
    
    # 모두 str으로 변환하자!
    dict = {'1': 'w', '-1': 's', '10':'d', '-10': 'a'}
    for i in range(len(numLog)-1):
        action = str(numLog[i+1]-numLog[i])
        #idea 1: if else
        #idea 2: map or zip
        #idea 3: dict
        answer.append(dict[action])
    return "".join(list(map(str, answer)))