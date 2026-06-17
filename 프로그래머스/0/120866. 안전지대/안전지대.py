def solution(board):
    n = len(board)
    result = 0
    bomb = []

    # 지뢰 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb.append((i,j))

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for i, j in bomb:
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                pass

    return sum(row.count(0) for row in board)