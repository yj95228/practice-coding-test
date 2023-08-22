# https://www.acmicpc.net/problem/2667
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def bfs(r,c):
    queue = [(r,c)]
    result = 1
    while queue:
        r, c = queue.pop(0)
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            if 0 <= r+dx < N and 0 <= c+dy < N\
            and not visited[r+dx][c+dy] and matrix[r+dx][c+dy] == '1':
                visited[r+dx][c+dy] = True
                result += 1
                queue.append((r+dx, c+dy))
    return result

N = int(input())
matrix = list(input() for _ in range(N))
visited = [[False]*N for _ in range(N)]
answer = []
for r in range(N):
    for c in range(N):
        if not visited[r][c] and matrix[r][c] == '1':
            visited[r][c] = True
            answer.append(bfs(r,c))
print(len(answer))
print('\n'.join(map(str,sorted(answer))))