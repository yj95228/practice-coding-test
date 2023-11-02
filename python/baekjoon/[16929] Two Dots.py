import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c):
    global answer
    if answer == 'Yes': return
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == A[r][c]:
            if V[nx][ny]:
                if V[r][c]-V[nx][ny] >= 3:
                    answer = 'Yes'
                    return
                continue
            V[nx][ny] = V[r][c]+1
            dfs(nx, ny)
            V[nx][ny] = 0

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[0]*M for _ in range(N)]
answer = 'No'
for r in range(N):
    for c in range(M):
        V[r][c] = 1
        dfs(r, c)
        V[r][c] = 0
        if answer == 'Yes': break
    if answer == 'Yes': break
print(answer)