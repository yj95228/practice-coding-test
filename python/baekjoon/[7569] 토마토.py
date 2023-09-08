# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

M, N, H = map(int, input().split())
arr3d, queue = [], deque()
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
all_done = True
for h in range(H):
    arr2d = []
    for r in range(N):
        arr = list(map(int, input().split()))
        for c in range(M):
            if arr[c] == 1:
                queue.append((h,r,c))
                visited[h][r][c] = 1
            elif arr[c] == -1:
                visited[h][r][c] = -1
            else:
                all_done = False
        arr2d.append(arr)
    arr3d.append(arr2d)
if all_done: print(0)
else:
    while queue:
        h, r, c = queue.popleft()
        for dh, dx, dy in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
            if 0 <= h+dh < H and 0 <= r+dx < N and 0 <= c+dy < M\
            and not visited[h+dh][r+dx][c+dy] and arr3d[h+dh][r+dx][c+dy] >= 0:
                visited[h+dh][r+dx][c+dy] = visited[h][r][c] + 1
                queue.append((h+dh,r+dx,c+dy))
    tomato = sum(sum(visited,[]),[])
    print(-1 if 0 in tomato else max(tomato)-1)