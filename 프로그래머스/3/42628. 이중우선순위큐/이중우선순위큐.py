# import heapq

# def solution(operations):
#     signal_min = []
#     signal_max = []
#     pivot = 0
#     for op in operations:
#         if op[0] == "I":
#             direct, num = op.split(" ")
#             num = int(num)
#             if num < pivot:
#                 heapq.heappush(signal_min,int(num))
#             else:
#                 heapq.heappush(signal_max, -int(num))
#         elif op == "D 1":
#             if signal_max:
#                 heapq.heappop(signal_max)
#             else:
                
#         elif op == "D -1":
#             if signal_min:
#                 heapq.heappop(signal_min)
#             else:
                
#     if len(signal_min) + len(signal_max) == 0:
#         return [0,0]
#     else:
#         return [-heapq.heappop(signal_neg),heapq.heappop(signal)]

import heapq

def solution(operations):
    signal = []
    signal_neg = []
    for op in operations:
        if op == "D 1":
            if signal:
                max_neg = heapq.heappop(signal_neg)
                del signal[signal.index(-max_neg)]
        elif op == "D -1":
            if signal:
                min_pos = heapq.heappop(signal)
                del signal_neg[signal_neg.index(-min_pos)]
        elif op[0] == "I":
            direct, num = op.split(" ")
            heapq.heappush(signal,int(num))
            heapq.heappush(signal_neg, -int(num))
    if not signal:
        return [0,0]
    else:
        return [-heapq.heappop(signal_neg),heapq.heappop(signal)]