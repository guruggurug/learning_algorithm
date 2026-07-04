def solution(n):
    # 밑변이 n, 높이가 n인 삼각형 2차원 배열
    field = [[0]*i for i in range(1,n+1)]
    # field = [[0]*n]*n
    
    # column 고정하고 row 아래로 갔다가 오른쪽으로 갔다가 위로 갔다가 아래로 반복
    # 단, (0, n-1) > (1, n-2) > ... 범위가 좁혀진다.
    
    # 아래, 오른쪽, 위 반복 -> 3으로 나눈 나머지로 처리    
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    i = 0
    
    r, c = 0, 0
    
    r_uboundary, r_lboundary = 0, 0
    c_boundary = 0
    
    for num in range(1,n*(n+1)//2+1):
        field[r][c] = num
        
        nr = r + dr[i]
        nc = c + dc[i]
        
        if nr == r_uboundary or nc == n-c_boundary or nr == n-r_lboundary:
            i = (i+1) % 3
            if i == 0:
                r_uboundary += 2
                r_lboundary += 1
                c_boundary += 2
            nr = r + dr[i]
            nc = c + dc[i]

        r = nr
        c = nc
    
    answer = []
    for i in field:
        answer += i
            
    return answer