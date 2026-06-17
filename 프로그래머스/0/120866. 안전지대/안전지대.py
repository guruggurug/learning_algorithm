def solution(board):
    #[[0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0]]
    
    # 지뢰의 위치 [3][2]
    # 상하 탐색 [2][2] [4][2] ---> [i][j]에서 [i-1] & [i+1]
    # 좌우 탐색 [3][1] [3][3] ---> [i][j]에서 [j-1] & [j+1]
    # 대각선 탐색 ---> 좌우상하 탐색의 조합
    
    # 아이디어 1: 원소 하나씩 살펴보며 좌우상하, 대각선에 1이 있는지 확인
    n = len(board)
    result = 0
    for i in range(n):
        for j in range(n):
            flag = 0
            if board[i][j] == 1:
                print('지뢰', i, j)
                continue
            ind = {i:[], j:[]}
            for x in [-1,+1]:
                ind[i] += [i+x] if i+x >= 0 and i+x <= n-1 else []
                ind[j] += [j+x] if j+x >= 0 and j+x <= n-1 else []
            # {3: [2,4], 2: [1,3]}
            
            region = []
            region += [(i,x) for x in ind[j]]
            region += [(x,j) for x in ind[i]]
            region += [(x,y) for x in ind[i] for y in ind[j]]
            # region = [(3,1) (3,3), (2,2) (4,2), ...]
            print(i,j, '살펴보는 중..', region)
            for x, y in region:
                if board[x][y] == 1:
                    flag = 1
                    print('삐빕', i, j)
            if flag == 0:
                result += 1 # result += 1은 언제 해야 하는가....
    return result