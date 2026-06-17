# 나의 풀이 2
def solution(board):
    #[[0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0]]
    
    # 지뢰의 위치 [3][2]

    n = len(board)
    result = 0
    bomb = []

    # 지뢰 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb.append((i,j))
                # bomb 예시 결과 [(3,2)]
    
    # 상하 탐색 [2][2] [4][2] ---> [i][j]에서 [i-1] & [i+1]
    # 좌우 탐색 [3][1] [3][3] ---> [i][j]에서 [j-1] & [j+1]
    # 대각선 탐색 ---> [i-1] & [i+1] / [j-1] & [j+1]의 조합

    # 인접 지역 좌표 구하기
    region = []
    for x, y in bomb:
        for m in [-1,+1]:
            region += [(x, y+m), (x+m, y), (x+m, y+m), (x-m, y+m)]
            print(region)
            # region 예시 결과 [()]

    # 인접 지역 데이터 1로 바꾸기
    for x, y in region:
        print(x,y)
        if x in range(n) and y in range(n):
            board[x][y] = 1
    
    print(board)

    # 안전 지대 구하기
    return n*n - sum([sum(i) for i in board])