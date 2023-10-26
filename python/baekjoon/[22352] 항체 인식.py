from sys import stdin
input = stdin.readline

def dfs(x, y):
    stack = [(x, y)]
    V[x][y] = 1
    num = A[x][y]
    lst = [(x, y)]
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M and not V[nx][ny] and A[nx][ny] == num:
                V[nx][ny] = 1
                stack.append((nx, ny))
                lst.append((nx, ny))
    groups.append(lst)

def solve():
    change = False

    for group in groups:
        r, c = group[0]
        num1, num2 = A[r][c], B[r][c]

        for r, c in group:
            # 같은 영역에 색이 다르게 바뀐게 있으면
            if num2 != B[r][c]: return 'NO'

        if num1 != num2:
            # 색이 바뀐 영역이 여러 군데면
            if change: return 'NO'
            change = True

    return 'YES'

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
V = [[0]*M for _ in range(N)]
groups = []
for r in range(N):
    for c in range(M):
        if not V[r][c]:
            dfs(r, c)
print(solve())