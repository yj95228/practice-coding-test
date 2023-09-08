# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
import sys
sys.stdin = open('input.txt', 'r')

def bfs(R,C):
    visited = [[False]*M for _ in range(N)]
    visited[R][C] = True
    queue = [(R,C,1)]
    while queue:
        r,c,d = queue.pop(0)
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            if 0 <= r+dx < N and 0 <= c+dy < M and\
            not visited[r+dx][c+dy] and matrix[r+dx][c+dy]:
                visited[r+dx][c+dy] = True
                print(r+dx, c+dy, d)
                queue.append((r+dx,c+dy,d+1))
    return (R,C,d)

TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    for r in range(N):
        for c in range(M):
            if matrix[r][c]:
                answer.append(bfs(r,c))
    answer.sort(key=lambda x: (-x[2], x[0]+x[1], x[0]))
    print(f'#{tc} {answer[0][0]+1} {answer[0][1]+1}')