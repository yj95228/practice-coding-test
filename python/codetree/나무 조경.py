def recur(n, cnt, sm):
    global answer
    answer = max(answer, sm)
    if n == N*N or cnt == 4: return
    r, c = n//N, n%N
    recur(n+1, cnt, sm)
    if not V[r][c]:
        V[r][c] = 1
        for dx, dy in ((1,0),(0,1)):
            nx, ny = r+dx, c+dy
            if nx < N and ny < N and not V[nx][ny]:
                V[nx][ny] = 1
                recur(n+1, cnt+1, sm+A[r][c]+A[nx][ny])
                V[nx][ny] = 0
        V[r][c] = 0

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
V = [[0]*N for _ in range(N)]
answer = 0
recur(0, 0, 0)
print(answer)