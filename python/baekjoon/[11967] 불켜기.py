'''
- 1차. 스위치가 여러 개 있을 수 있으므로 스위치를 set()으로 처리했으나 틀림
- 2차. 알고리즘 엿보고 DFS -> BFS로 바꿈
- 3차. 불 킨 곳을 내가 갈 수 있으면 다시 가볼 수 있게 처리 (이거때문에 dfs로 했었음)
'''
# https://www.acmicpc.net/problem/7490
import sys
from collections import deque
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[False]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
A[0][0] = True
answer = 1

switch = dict()
for _ in range(M):
    x, y, a, b = map(lambda x: int(x)-1, input().split())
    if (x,y) in switch:
        switch[(x,y)].add((a,b))
    else:
        switch[(x,y)] = set([(a,b)])

if (0,0) in switch:
    for r,c in switch[(0,0)]:
        A[r][c] = True
        answer += 1
        
queue = deque([(0,0)])
while queue:
    r, c = queue.popleft()
    
    # 갔으면 불키자
    if (r,c) in switch:
        for x, y in switch[(r,c)]:
            if A[x][y]: continue
            answer += 1
            A[x][y] = True

            # 혹시 불 킨 곳을 내가 갈 수 있는 곳이면 가보자
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                rr, cc = x+dx, y+dy
                if 0 <= rr < N and 0 <= cc < N and visited[rr][cc]:
                    queue.append((rr,cc))

    # 상하좌우 인접한 곳만 갈 수 있어
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and A[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx,ny))

print(answer)

# 2차 풀이
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[0] * N for _ in range(N)]
obj = dict()
for _ in range(M):
    x, y, a, b = map(lambda x: int(x) - 1, input().split())
    if (x, y) == (a, b): continue
    if obj.get((x, y)):
        obj[(x, y)].add((a, b))
    else:
        obj[(x, y)] = {(a, b)}

answer = 1
queue = {(0, 0)}
V = [[0] * N for _ in range(N)]
A[0][0] = V[0][0] = 1
for r, c in obj[(0, 0)]:
    if A[r][c]: continue
    A[r][c] = 1
    answer += 1
while queue:
    next_q = set()
    for r, c in queue:
        if obj.get((r, c)):
            for rr, cc in obj[(r, c)]:
                if A[rr][cc]: continue
                A[rr][cc] = 1
                answer += 1
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx, ny = rr + dx, cc + dy
                    if 0 <= nx < N and 0 <= ny < N and V[nx][ny]:
                        next_q.add((nx, ny))
                        break
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = r + dx, c + dy
            if 0 <= nx < N and 0 <= ny < N and not V[nx][ny] and A[nx][ny]:
                V[nx][ny] = 1
                next_q.add((nx, ny))
    queue = next_q
print(answer)