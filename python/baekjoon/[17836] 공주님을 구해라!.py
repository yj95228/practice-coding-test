# https://www.acmicpc.net/problem/17836
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M, T = map(int, input().split())
matrix = [list(input().split()) for _ in range(N)]
visited = [[[False]*M for _ in range(N)] for _ in range(2)]
queue = deque([(False,0,0,0)])
visited[False][0][0] = True

while queue:
    gram, r, c, time = queue.popleft()
    if time > T:
        print('Fail')
        break
    elif (r,c) == (N-1,M-1):
        print(time)
        break
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < M and not visited[gram][nx][ny]\
        and (gram or matrix[nx][ny] != '1'):
            gram = gram or matrix[nx][ny] == '2'
            visited[gram][nx][ny] = True
            queue.append((gram, nx, ny, time+1))
# 1차 시도에서 빠뜨린 부분
else: print('Fail')