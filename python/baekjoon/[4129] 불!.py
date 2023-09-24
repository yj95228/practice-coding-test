# https://www.acmicpc.net/problem/4129
'''
1차 제출: (187480kb, 572ms) 불을 먼저 움직이게 하고 지훈이를 나중에 움직이게 하는 식으로 함
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    time = 0
    while queue:
        time += 1
        for _ in range(len(queue)):
            where, r, c = queue.popleft()
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if where == FIRE:
                    if 0 <= nx < R and 0 <= ny < C and (A[nx][ny] == BLANK or A[nx][ny] == JIHOON):
                        A[nx][ny] = FIRE
                        queue.append((FIRE,nx,ny))
                elif where == JIHOON:
                    if 0 <= nx < R and 0 <= ny < C:
                        if A[nx][ny] == BLANK:
                            A[nx][ny] = JIHOON
                            queue.append((JIHOON,nx,ny))
                    else:
                        return time
    return 'IMPOSSIBLE'

R, C = map(int, input().split())
A = [list(input().rstrip()) for _ in range(R)]
queue = deque()

WALL, BLANK, JIHOON, FIRE = '#', '.', 'J', 'F'
visited = [[0]*C for _ in range(R)]
F = [[0]*C for _ in range(R)]

jr, jc = None, None
for r in range(R):
    for c in range(C):
        if A[r][c] == FIRE:
            queue.append((FIRE, r, c))
        elif A[r][c] == JIHOON:
            jr, jc = r, c
queue.append((JIHOON, jr, jc))

print(bfs())