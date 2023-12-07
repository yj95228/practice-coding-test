import sys
from itertools import combinations
input = sys.stdin.readline

def solve(green, red):
    V = [[0]*M for _ in range(N)]
    queue = []
    for r, c in green:
        V[r][c] = 1
        queue.append((1, r, c))
    for r, c in red:
        V[r][c] = 2
        queue.append((2, r, c))
    cnt = 0
    while queue:
        next_q = []
        visited = set()
        for color, r, c in queue:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and A[nx][ny]:
                    if color + V[nx][ny] == 3:
                        if (nx, ny) in visited:
                            cnt += 1
                            V[nx][ny] += color
                            next_q.remove((3-color, nx, ny))
                    elif not V[nx][ny]:
                        visited.add((nx, ny))
                        V[nx][ny] = color
                        next_q.append((color, nx, ny))
        queue = next_q
    return cnt

def recur(n, green, red, arr):
    global answer
    if n == len(arr):
        if len(green) == G and len(red) == R:
            answer = max(answer, solve(green, red))
        return
    r, c = arr[n]
    recur(n+1, green+[(r, c)], red, arr)
    recur(n+1, green, red+[(r, c)], arr)

N, M, G, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
can = []
for r in range(N):
    for c in range(M):
        if A[r][c] == 2:
            can.append((r, c))
answer = 0
for arr in combinations(can, G+R):
    recur(0, [], [], arr)
print(answer)