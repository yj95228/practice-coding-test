# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq
def recur(n, r, c, k, prev, gongsa):
    global answer
    answer = max(answer, n)
    if prev == 0: return
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if matrix[nx][ny] < prev:
                visited[nx][ny] = True
                recur(n+1, nx, ny, k, matrix[nx][ny], gongsa)
                visited[nx][ny] = False
            elif not gongsa and matrix[nx][ny] - prev <= k-1:
                visited[nx][ny] = True
                recur(n+1, nx, ny, k-(matrix[nx][ny]-prev+1), prev-1, True)
                visited[nx][ny] = False

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    mx = 0
    for r in range(N):
        for c in range(N):
            mx = max(mx, matrix[r][c])
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == mx:
                visited = [[False]*N for _ in range(N)]
                visited[r][c] = True
                recur(1, r, c, K, matrix[r][c], False)
    print(f'#{tc} {answer}')