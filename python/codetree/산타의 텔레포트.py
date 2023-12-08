import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def bfs(sr, sc, eer, eec):
    V = [[987654321] * (M+2) for _ in range(N+2)]
    V[sr][sc] = 0
    queue = [(0, sr, sc)]
    teleport = [0]*(mx+1)
    while queue:
        energy, r, c = heappop(queue)
        if (r, c) == (eer, eec): return energy
        if energy > V[r][c]: continue
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if energy < V[nx][ny] and A[nx][ny] != -1:
                V[nx][ny] = energy
                heappush(queue, (energy, nx, ny))
                if A[nx][ny] >= 10:
                    if teleport[A[nx][ny]]: continue
                    teleport[A[nx][ny]] = 1
                    for rr, cc in obj[A[nx][ny]]:
                        if energy+1 < V[rr][cc]:
                            V[rr][cc] = energy+1
                            heappush(queue, (energy+1, rr, cc))
    return -1

def solve():
    answer = 0
    energy = bfs(1, 1, er, ec)
    if energy == -1: return -1
    answer += energy
    energy = bfs(er, ec, N, M)
    if energy == -1: return -1
    answer += energy
    return answer

N, M = map(int, input().split())
A = [[-1]*(M+2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1]*(M+2)]
er, ec = -1, -1
obj = dict()
mx = 0
for r in range(1, N+1):
    for c in range(1, M+1):
        if A[r][c] == -2:
            er, ec = r, c
            A[r][c] = 0
        elif A[r][c] >= 10:
            mx = max(mx, A[r][c])
            if obj.get(A[r][c]):
                obj[A[r][c]] += [(r, c)]
            else:
                obj[A[r][c]] = [(r, c)]
print(solve())