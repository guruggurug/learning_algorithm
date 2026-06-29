def walking(location, move, park_map, size):
    
    N = int(move[1])
    
    x = location[1]
    y = location[0]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    op = {"E": 0, "W": 1, "S": 2, "N": 3}
    i = op[move[0]]
    
    for n in range(N):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx>=size[0] or ny>=size[1] or nx<0 or ny<0:
            return location
        if park_map[ny][nx] == "X":
            return location
        
        x = nx
        y = ny
    
    return [ny,nx]
    
def solution(park, routes):
    # ["OSO",
    # "OOO",
    # "OXO",
    # "OOO"]
    
    # 방향벡터 매핑
    # S / N / E / W
    # dx = [1,-1,0,0]
    # dy = [0,0,1,-1]
    
    park_map = []
    obstacles = []
    size = (len(park[0]), len(park))
    
    for i in range(len(park)):
        i_split = list(park[i])
        if "S" in park[i]:
            location = (i, i_split.index("S"))
        # if "X" in park[i]:
        #     for j in range(len(i_split)):
        #         if i_split[j] == "X":
        #             obstacles += [(i,j)]
        park_map += [i_split]
    
    moves = [(route.split(" ")) for route in routes]
    print(moves)
    
    for move in moves:
        print('current', location)
        location = walking(location, move, park_map, size)
        print('moved', location)

    return location
    
    