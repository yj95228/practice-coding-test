# https://www.acmicpc.net/problem/2636
import sys
import copy
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

R, C = map(int, input().split())
cheese = [list(input().split()) for _ in range(R)]
air = [[False]*C for _ in range(R)]
# answer: 시간, result: 치즈 칸 갯수
answer, result = 0, sum([x == '1' for row in cheese for x in row])

while result:
    # (1) 공기 확인
    queue = deque([(0,0)])
    air = [[False]*C for _ in range(R)]
    air[0][0] = True
    while queue:
        r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < R and 0 <= ny < C and not air[nx][ny] and cheese[nx][ny] == '0':
                air[nx][ny] = True
                queue.append((nx,ny))

    # (2) 치즈 녹이기
    melt = 0
    new_cheese = copy.deepcopy(cheese)
    new_air = copy.deepcopy(air)
    for r in range(R):
        for c in range(C):
            if cheese[r][c] == '1':
                air_touch = 0
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < R and 0 <= ny < C and air[nx][ny]:
                        air_touch += 1
                    if air_touch >= 2:
                        new_air[r][c] = True
                        new_cheese[r][c] = '0'
                        melt += 1
                        break

    answer += 1
    result -= melt
    cheese = copy.deepcopy(new_cheese)

print(answer)