import heapq

def solution(scoville, K):
    count = 0
    repeat = len(scoville)
    heapq.heapify(scoville)
    while True:
        food = heapq.heappop(scoville)
        if food < K:
            food2 = heapq.heappop(scoville)
            heapq.heappush(scoville,food + food2*2)
            count += 1
        else:
            return count
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1