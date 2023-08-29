# TODO: 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
# 비활성 바이러스가 활성화되지 않아도 ㄱㅊ
# https://www.acmicpc.net/problem/17142
import sys
import copy
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def bfs(arr):
    mx = 0
    queue = deque(arr)
    visited = copy.deepcopy(matrix)
    for r,c in virus:
        visited[r][c] = 1 if (r,c) in arr else 0
    while queue:
        time, r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and matrix[nx][ny] in (0,2):
                if matrix[nx][ny] == 0: mx = max(mx, time+1)
                visited[nx][ny] = 1
                queue.append((time+1, nx, ny))
    for r,c in virus:
        visited[r][c] = 1
    return min(sum(visited,[])), mx


def dfs(arr):
    if len(arr) == M:
        virus_list.append(list(map(lambda x: (0,*virus[x]), arr)))
        return
    for x in range(len(virus)):
        if not arr or arr[-1] < x:
            dfs(arr+[x])

N, M = map(int, input().split())
matrix = []
virus = []
for r in range(N):
    arr = list(map(int, input().split()))
    if 2 in arr:
        for c in range(N):
            if arr[c] == 2:
                virus.append((r,c))
    matrix.append(arr)

virus_list = []
dfs([])

cannot, answer = 0, 987654321
for v in virus_list:
    mn, mx = bfs(v)
    cannot = max(cannot, mn)
    if mn: answer = min(answer, mx)
print(answer if cannot else -1)