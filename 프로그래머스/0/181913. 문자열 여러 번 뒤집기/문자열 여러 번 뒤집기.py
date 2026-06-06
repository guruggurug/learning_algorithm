def solution(my_string, queries):
    my_string = list(map(str, my_string))
    for query in queries:
        s=query[0]
        e=query[1]
        temp=my_string[s:e+1]
        temp.reverse()
        my_string[s:e+1]=temp
    return "".join(my_string)