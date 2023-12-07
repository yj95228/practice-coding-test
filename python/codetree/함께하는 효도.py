import sys
input = sys.stdin.readline

def recur(n, m, r, c, sm):
    if n == 3:
        n, m = 0, m+1
        if m == M:
            global answer
            answer = max(answer, sm)
            return
        else:
            r, c = friends[m]
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N:
            if V[nx][ny]:
                recur(n+1, m, nx, ny, sm)
            else:
                V[nx][ny] = 1
                recur(n+1, m, nx, ny, sm+A[nx][ny])
                V[nx][ny] = 0


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
V = [[0]*N for _ in range(N)]
friends = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
answer = 0
for r, c in friends:
    V[r][c] = 1
    answer += A[r][c]
recur(0, 0, friends[0][0], friends[0][1], answer)
print(answer)