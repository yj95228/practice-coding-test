# DFS로 풀었다가 recursion error 떠서 bfs로 수정
# https://www.acmicpc.net/problem/16954
from sys import stdin
from collections import deque
input = stdin.readline

matrix = [list(input().rstrip()) for _ in range(8)]
answer = 0
queue = deque([(7,0)])
while queue:
    if answer: break
    for _ in range(len(queue)):
        r, c = queue.popleft()
        if (r,c) == (0,7):
            answer = 1
            break
        elif matrix[r][c] == '#': continue
        for dx, dy in ((-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(0,0)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < 8 and 0 <= ny < 8 and matrix[nx][ny] == '.':
                queue.append((nx,ny))
    matrix = [['.']*8] + matrix[:-1]
print(answer)