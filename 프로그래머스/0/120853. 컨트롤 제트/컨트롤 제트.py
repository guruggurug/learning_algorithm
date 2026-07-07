def solution(s):
    moves = s.split(" ")
    for i in range(len(moves)):
        if moves[i] == "Z":
            moves[i-1:i+1] = [0,0]
        else:
            moves[i] = int(moves[i])
    return sum(moves)
    