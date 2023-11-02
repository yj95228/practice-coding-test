from sys import stdin
input = stdin.readline

def bfs(i, j):
    (sr, sc), (er, ec) = items[i], items[j]
    queue = [(sr, sc)]
    V = [[0]*M for _ in range(N)]
    V[sr][sc] = 1
    while queue:
        temp_q = []
        for r, c in queue:
            if (r, c) == (er, ec):
                return V[r][c]-1
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and not V[nx][ny] and A[nx][ny] != '#':
                    V[nx][ny] = V[r][c] + 1
                    temp_q.append((nx, ny))
        queue = temp_q
    return 987654321

def recur(n, arr):
    global answer
    if n == item:
        arr += [item+1]
        result = 0
        for i in range(item+1):
            if D[arr[i]][arr[i+1]] == 987654321:
                return
            result += D[arr[i]][arr[i+1]]
        answer = min(answer, result)
        return
    for x in range(1, item+1):
        if visited[x]: continue
        visited[x] = 1
        recur(n+1, arr+[x])
        visited[x] = 0

M, N = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
sr, sc, er, ec = None, None, None, None
items, item = [], 0
for r in range(N):
    for c in range(M):
        if A[r][c] == 'S':
            sr, sc = r, c
            A[r][c] = 'X'
        elif A[r][c] == 'E':
            er, ec = r, c
            A[r][c] = 'X'
        elif A[r][c] == 'X':
            items.append((r, c))
            item += 1
items.insert(0, (sr, sc))
items.append((er, ec))

D = [[987654321]*(item+2) for _ in range(item+2)]
for x in range(item+2):
    D[x][x] = 0
for i in range(item+1):
    for j in range(i+1, item+2):
        dist = bfs(i, j)
        D[i][j] = dist
        D[j][i] = dist

visited = [0]*(item+1)
answer = 987654321
recur(0, [0])
print(answer)