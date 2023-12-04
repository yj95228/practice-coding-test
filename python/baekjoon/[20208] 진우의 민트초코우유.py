import sys
input = sys.stdin.readline

def recur(n, cnt, hp, r, c):
    global answer
    if abs(r-sr)+abs(c-sc) <= hp:
        answer = max(answer, cnt)
    if n == length: return
    for i in range(1, length):
        if V[i]: continue
        V[i] = 1
        nx, ny = milk[i]
        d = abs(nx-r)+abs(ny-c)
        if d <= hp: recur(n+1, cnt+1, hp-d+H, nx, ny)
        V[i] = 0

N, M, H = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
V = [[0]*N for _ in range(N)]
milk = []
sr, sc = -1, -1
for r in range(N):
    for c in range(N):
        if A[r][c] == 1:
            sr, sc = r, c
        elif A[r][c] == 2:
            milk.append((r, c))
milk.insert(0, (sr, sc))

answer = 0
length = len(milk)
V = [0]*length
recur(0, 0, M, sr, sc)
print(answer)