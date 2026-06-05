def solution(arr, queries):
    #아이디어 1: 조건 그대로 구현
    #queries에서 query를 하나씩 꺼낸다 > 반복문
    #arr의 두 원소를 바꾼다 > temp 변수 필요
    temp = 0
    for i, j in queries:
        temp =arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr