def bfs(x, y):
    global level, eat, sr, sc
    V = [[0]*N for _ in range(N)]
    V[x][y] = 1
    queue = [(x, y)]
    turn = 0
    while queue:
        next_q, monster = [], []
        for r, c in queue:
            for dx, dy in ((1,0),(0,-1),(0,1),(-1,0)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not V[nx][ny] and level >= A[nx][ny]:
                    V[nx][ny] = 1
                    if level > A[nx][ny] > 0:
                        monster.append((nx, ny))
                    next_q.append((nx, ny))
        if monster:
            r, c = sorted(monster)[0]
            A[r][c] = 0
            sr, sc = r, c
            eat += 1
            if level == eat:
                level, eat = level+1, 0
            return turn+1
        turn += 1
        queue = next_q
    return 0

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
level, eat = 2, 0
sr, sc = None, None
for r in range(N):
    for c in range(N):
        if A[r][c] == 9:
            sr, sc = r, c
            A[r][c] = 0

time = 0
while True:
    result = bfs(sr, sc)
    if result:
        time += result
    else:
        print(time)
        break