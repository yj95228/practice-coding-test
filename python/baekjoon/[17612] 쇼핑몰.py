import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int, input().split())
enter = [(0, x) for x in range(1, K+1)]
end = []
answer = 0
for _ in range(N):
    id, w = map(int, input().split())
    time, cart = heappop(enter)
    heappush(enter, (time+w, cart))
    heappush(end, (time+w, -cart, id))
for x in range(1, N+1):
    time, cart, id = heappop(end)
    answer += id*x
print(answer)