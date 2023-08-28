# https://www.acmicpc.net/problem/23747
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def bfs(x,y):
    visited[x][y] = True
    queue = deque([(x,y)])
    while queue:
        r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < R and 0 <= ny < C and\
            not visited[nx][ny] and matrix[nx][ny] == matrix[x][y]:
                visited[nx][ny] = True
                answer[nx][ny] = '.'
                queue.append((nx, ny))
    answer[x][y] = '.'

R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
answer = [['#']*C for _ in range(R)]
r, c = map(lambda x: int(x)-1, input().split())
for x in list(input().rstrip()):
    if x == 'W':
        if not visited[r][c] and answer[r][c] != '.': bfs(r,c)
    elif x == 'L': c -= 1
    elif x == 'R': c += 1
    elif x == 'U': r -= 1
    elif x == 'D': r += 1

answer[r][c] = '.'
for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
    nx, ny = r+dx, c+dy
    if 0 <= nx < R and 0 <= ny < C:
        answer[nx][ny] = '.'

for a in answer:
    print(''.join(a))