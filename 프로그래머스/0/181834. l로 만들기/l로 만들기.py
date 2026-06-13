def solution(myString):
    myList = list(myString)
    answer = []
    # print(ord('l'))
    for i in myList:
        if ord(i) < 108:
            answer.append('l')
        else:
            answer.append(i)
    return "".join(answer)