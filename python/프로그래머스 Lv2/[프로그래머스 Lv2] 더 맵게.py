# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3

import heapq
from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return answer
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        answer += 1
        heappush(scoville, heappop(scoville) + heappop(scoville)*2)
    return answer
