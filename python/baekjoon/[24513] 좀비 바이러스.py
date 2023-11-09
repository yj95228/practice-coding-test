# https://www.acmicpc.net/problem/24513
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[-1]*(M+2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1]*(M+2)]
V = [[0]*(M+2) for _ in range(N+2)]
queue = []
for r in range(1, N+1):
    for c in range(1, M+1):
        if 1 <= A[r][c] <= 2:
            queue.append((A[r][c], r, c))
            V[r][c] = 1

while queue:
    temp_q = set()
    for virus, r, c in queue:
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if not V[nx][ny] and not A[nx][ny]:
                temp_q.add((virus, nx, ny))
    next_q = []
    for virus, r, c in temp_q:
        V[r][c] = 1
        if A[r][c]:
            A[r][c] = 3
            next_q.remove((3-virus, r, c))
        else:
            A[r][c] = virus
            next_q.append((virus, r, c))
    queue = next_q

answer = [0]*3
for r in range(1, N+1):
    for c in range(1, M+1):
        if 1 <= A[r][c] <= 3:
            answer[A[r][c]-1] += 1
print(*answer)