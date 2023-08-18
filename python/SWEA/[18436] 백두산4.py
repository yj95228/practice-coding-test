# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
sys.stdin = open('input.txt', 'r')

def bfs(x,y,num):
    queue = [(x,y)]
    while queue:
        r, c = queue.pop(0)
        matrix[r][c] = num
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            if 0 <= r+dx < N and 0 <= c+dy < M and\
            not visited[r+dx][c+dy] and matrix[r+dx][c+dy]:
                visited[r+dx][c+dy] = True
                queue.append((r+dx,c+dy))

def dijkstra(x,y,num):
    visited = [[False]*M for _ in range(N)]
    queue = [(0,x,y)]
    visited[x][y] = True
    while queue:
        weight, r, c = queue.pop(0)
        if matrix[r][c]:
            distance[num][matrix[r][c]-1] = min(weight, distance[num][matrix[r][c]-1])
            distance[matrix[r][c]][num-1] = min(weight, distance[matrix[r][c]][num-1])
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            if 0 <= r+dx < N and 0 <= c+dy < M and not visited[r+dx][c+dy]:
                visited[r+dx][c+dy] = True
                if matrix[r+dx][c+dy] != num:
                    queue.append((weight+1, r+dx,c+dy))
                else: queue.append((weight, r+dx,c+dy))

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    num = 1
    magma_list = []
    for r in range(N):
        for c in range(M):
            if matrix[r][c] and not visited[r][c]:
                magma_list.append((r,c,num))
                bfs(r,c,num)
                num += 1
            visited[r][c] = True

    distance = {x: [N*M]*(num-1) for x in range(1,num)}
    for x in range(1,num):
        distance[x][x-1] = 0

    for r in range(N):
        for c in range(M):
            if matrix[r][c]:
                dijkstra(r,c,matrix[r][c])

    mx_idx, mx = 0, 0
    for k, v in distance.items():
        if mx < max(v):
            mx = max(v)
            mx_idx = k
    print(f'#{tc} {magma_list[mx_idx-1][0]+1} {magma_list[mx_idx-1][1]+1}')