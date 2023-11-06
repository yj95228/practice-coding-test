N, M = map(int, input().split())
sr, sc, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dt = ((-1,0),(0,1),(1,0),(0,-1))
answer = 1
A[sr][sc] = 2
while True:
    for i in range(1, 5):
        nd = (d-i)%4
        dx, dy = dt[nd]
        nx, ny = sr+dx, sc+dy
        if not A[nx][ny]:
            A[nx][ny] = 2
            answer += 1
            sr, sc, d = nx, ny, nd
            break
    else:
        dx, dy = dt[d]
        nx, ny = sr-dx, sc-dy
        if A[nx][ny] != 1:
            if not A[nx][ny]: answer += 1
            A[nx][ny] = 2
            sr, sc = nx, ny
        else: break
print(answer)