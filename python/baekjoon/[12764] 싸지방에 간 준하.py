# https://www.acmicpc.net/problem/12764
import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    P, Q = map(int, input().split())
    heappush(queue, (P,Q))
time, answer = [-1], [0]
while queue:
    start, end = heappop(queue)
    for i,x in enumerate(time):
        if x <= start:
            time[i] = end
            answer[i] += 1
            break
    else:
        time.append(end)
        answer.append(1)
print(len(time))
print(*answer)