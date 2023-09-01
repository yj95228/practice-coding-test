# FIXME: 집집마다 치킨집 거리를 확인해서 시간초과
# 치킨집에서 집까지의 거리를 BFS로 풀었음
# 굳이 BFS 할 필요도 없었고 집에서 치킨집 거리 최솟값 저장
# https://www.acmicpc.net/problem/15686
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def bfs(arr):
    queue = deque(arr)
    visited = [[0]*N for _ in range(N)]
    for r, c in queue:
        visited[r][c] = 1
    while queue:
        r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(0,-1),(-1,0)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = visited[r][c] + 1
                queue.append((nx,ny))
    return sum([visited[r][c]-1 for r, c in house])

def dfs(arr, start, cnt):
    global answer
    if cnt == M:
        answer = min(answer, bfs(arr))
        return
    for x in range(start, len(chicken)):
        r, c = chicken[x]
        matrix[r][c] = '2'
        dfs(arr+[(r,c)], x+1, cnt+1)
        matrix[r][c] = '0'

N, M = map(int, input().split())
matrix = []
chicken = []
house = []
answer = 987654321
for r in range(N):
    arr = list(input().split())
    for c in range(N):
        if arr[c] == '2':
            chicken.append((r,c))
            arr[c] = '0'
        elif arr[c] == '1':
            house.append((r,c))
    matrix.append(arr)

dfs([],0,0)
print(answer)