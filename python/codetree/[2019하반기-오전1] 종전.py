def solve(x, y, d1, d2):
    B = [[0]*N for _ in range(N)]
    def dfs(x, y, num, sr, er, sc, ec):
        B[x][y] = num
        stack = [(x, y)]
        while stack:
            r, c = stack.pop()
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if sr <= nx <= er and sc <= ny <= ec and not B[nx][ny]:
                    B[nx][ny] = num
                    stack.append((nx, ny))

    for _ in range(d1):
        nx, ny = x+1, y-1
        B[nx][ny] = 1
        x, y = nx, ny
    for _ in range(d2):
        nx, ny = x+1, y+1
        B[nx][ny] = 1
        x, y = nx, ny
    for _ in range(d1):
        nx, ny = x-1, y+1
        B[nx][ny] = 1
        x, y = nx, ny
    for _ in range(d2):
        nx, ny = x-1, y-1
        B[nx][ny] = 1
        x, y = nx, ny
    dfs(0, 0, 2, 0, x+d1-1, 0, y)
    dfs(0, N-1, 3, 0, x+d2, x+1, N-1)
    dfs(N-1, 0, 4, x+d1, N-1, 0, y+d2-d1-1)
    dfs(N-1, N-1, 5, x+d2+1, N-1, y+d2-d1, N-1)
    for r in range(x, x+d1+d2):
        for c in range(y-d1, y+d2):
            if not B[r][c]:
                B[r][c] = 1
    result = [0]*5
    for r in range(N):
        for c in range(N):
            result[B[r][c]-1] += A[r][c]
    return max(result)-min(result)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dt = ((1,-1),(1,1),(-1,1),(-1,-1))
answer = 987654321
for r in range(N-2):
    for c in range(1, N-1):
        for d1 in range(1, c+1):
            for d2 in range(1, N-c):
                if r+d1+d2 >= N: continue
                answer = min(answer, solve(r, c, d1, d2))
print(answer)