def solution(n, stations, w):

    count = 0
    station_idx = 0

    if stations[0]-w<1:
        need_s = stations[0]+w+1
        station_idx = 1
    else:
        need_s = 1


    while station_idx < len(stations):
        s = stations[station_idx]
        block_start = s-w
        if need_s < block_start:
            count += (block_start-need_s-1) // (2*w+1) + 1
        need_s = s+w+1
        station_idx += 1

    if need_s <= n:
        count += (n-need_s) // (2*w+1) + 1
    
    return count