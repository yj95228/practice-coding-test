import sys
input = sys.stdin.readline

def bfs(x, y):
    sm = A[x][y]
    V[x][y] = 1
    queue = [(x, y)]
    lst = [(x, y)]
    while queue:
        next_q = []
        for r, c in queue:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not V[nx][ny] and A[nx][ny] == A[r][c]:
                    V[nx][ny] = 1
                    next_q.append((nx, ny))
                    lst.append((nx, ny))
                    sm += A[nx][ny]
        queue = next_q
    for r, c in lst:
        B[r][c] = sm

def play(sr, sc, sd, dice):
    global answer
    dx, dy = dt[sd]
    nx, ny = sr+dx, sc+dy
    if not (0 <= nx < N and 0 <= ny < N):
        sd = (sd+2)%4
        dx, dy = dt[sd]
        nx, ny = sr+dx, sc+dy

    answer += B[nx][ny]
    new_dice = list(map(lambda x: dice[rotate[sd][x]], range(6)))
    if new_dice[-1]+1 > A[nx][ny]:
        return nx, ny, (sd+1)%4, new_dice
    elif new_dice[-1]+1 < A[nx][ny]:
        return nx, ny, (sd-1)%4, new_dice
    else:
        return nx, ny, sd, new_dice

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dice = [0,1,2,3,4,5]    # 위(0), 앞(1), 오(2), 왼(3), 뒤(4), 밑(5)
dt = ((0,1),(1,0),(0,-1),(-1,0))
B = [[0]*N for _ in range(N)]
V = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not V[r][c]:
            bfs(r, c)
rotate = [
    [3,1,0,5,4,2],
    [4,0,2,3,5,1],
    [2,1,5,0,4,3],
    [1,5,2,3,0,4]
]
answer = 0
sr, sc, sd = 0, 0, 0
for _ in range(M):
    sr, sc, sd, dice = play(sr, sc, sd, dice)
print(answer)