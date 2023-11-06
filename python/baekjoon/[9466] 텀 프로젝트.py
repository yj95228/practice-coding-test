import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    rank = [0]*(N+1)
    for x in range(1, N+1):
        rank[arr[x]] += 1

    queue = deque()
    for x in range(1, N+1):
        if rank[x] == 0:
            queue.append(x)

    answer = 0
    while queue:
        x = queue.popleft()
        answer += 1
        v = arr[x]
        rank[v] -= 1
        if rank[v] == 0:
            queue.append(v)
    print(answer)