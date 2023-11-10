import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 프림
N = int(input())
arr = [int(input()) for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
V = [0]*N
answer = min(arr)
start = arr.index(answer)
queue = [(0, start)]
while queue:
    cost, current = heappop(queue)
    if not V[current]:
        V[current] = 1
        answer += cost
        for idx, x in enumerate(A[current]):
            if V[idx]: continue
            heappush(queue, (min(x, arr[idx]), idx))
print(answer)

# 크루스칼
def union(a, b):
    if find(a) == find(b):
        return False
    else:
        parents[find(b)] = find(a)
        return True

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

N = int(input())
arr = [int(input()) for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
parents = [x for x in range(N+1)]
for idx, x in enumerate(arr):
    A[idx].append(x)

MST = []
for r in range(N):
    for c in range(r+1, N+1):
        MST.append((r, c, A[r][c]))

MST.sort(key=lambda x: x[-1])

answer, cnt = 0, 0
for a, b, c in MST:
    if cnt == N: break
    if union(a, b):
        answer += c
        cnt += 1
print(answer)