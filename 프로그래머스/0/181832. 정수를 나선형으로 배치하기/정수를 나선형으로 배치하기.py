def solution(n):
    # 이차원 배열 생성
    result = [[0]*n for _ in range(n)]
    
    # [[0,0,0,0],
       # [0,0,0,0],
       # [0,0,0,0],
       # [0,0,0,0]]
    
    # 이차원 배열 국룰 방향 벡터 dx, dy 세팅
    # 우 > 하 > 좌 > 상
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    x,y = 0,0
    
    # 방향 벡터 전환용 변수
    dir = 0
    
    for num in range(1,n**2+1):
        result[x][y] = num
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n or result[nx][ny] != 0:
            
            dir = (dir + 1) % 4
            
            nx = x + dx[dir]
            ny = y + dy[dir]
        
        x = nx
        y = ny
    
    return result