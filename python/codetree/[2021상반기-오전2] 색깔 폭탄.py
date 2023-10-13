# https://www.codetree.ai/training-field/frequent-problems/problems/colored-bomb/description?page=1&pageSize=20
from sys import stdin
input = stdin.readline

def dfs(r,c,group):
    groups[r][c] = group
    cnt, rainbow, mr, mc, color = 1, 0, r, c, matrix[r][c]
    rainbows = []
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        if matrix[r][c] == 0:
            rainbow += 1
            rainbows.append((r, c))
        else:
            if mr < r:
                mr, mc = r, c
            elif mr == r:
                if c < mc: mc = c
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not groups[nx][ny] and\
            (matrix[nx][ny] == 0 or matrix[nx][ny] == color):
                groups[nx][ny] = group
                cnt += 1
                stack.append((nx, ny))
    for r, c in rainbows:
        groups[r][c] = 0
    if cnt > 1:
        return cnt, -rainbow, mr, -mc

def remove(r,c):
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    group = groups[r][c]
    matrix[r][c] = None
    stack = [(r,c)]
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and\
            (group == groups[nx][ny] or matrix[nx][ny] == 0):
                visited[nx][ny] = 1
                matrix[nx][ny] = None
                stack.append((nx, ny))

def down(matrix):
    for c in range(N):
        for r in range(N-1,-1,-1):
            if matrix[r][c] is None:
                now = r
                while 0 <= now-1 and matrix[now][c] is None:
                    now -= 1
                if matrix[now][c] != -1:
                    matrix[now][c], matrix[r][c] = matrix[r][c], matrix[now][c]

def rotate(matrix):
    narr = [[None]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            narr[r][c] = matrix[c][N-r-1]
    return narr


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    # 1. 폭탄 묶음 찾기
    groups = [[0]*N for _ in range(N)]
    group = 1
    block = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] is not None and matrix[r][c] > 0 and not groups[r][c]:
                result = dfs(r,c,group)
                if result: block.append(result)
                group += 1

    # 2. 선택된 폭탄 묶음 제거
    if block:
        cnt, _, r, c = max(block)
        answer += cnt**2
        remove(r, -c)
    else:
        print(answer)
        break

    # 3. 중력 작용
    down(matrix)

    # 4. 반시계 90도 회전
    matrix = rotate(matrix)

    # 5. 중력 작용
    down(matrix)