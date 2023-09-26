# 시간복잡도 : 5!(판 순서 정하기) * 2^10(각 판별 회전 정하기) * 5^3(BFS) = 약 10^7...?
# 판 순서 정하는거 놓침
# 처음과 도착지에 방문 못하면 or 최단 거리로 도착했다면 빨리 return시키기
# zip말고 배열 index로 회전시키면 더 빨랐을 듯
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def bfs(arr):
    if arr[0][0][0] == '0' or arr[-1][-1][-1] == '0': return 126
    visited = [[[126]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1
    queue = deque([(0,0,0)])
    while queue:
        h, r, c = queue.popleft()
        if (h,r,c) == (4,4,4):
            return visited[h][r][c]
        for dx, dy, dz in ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)):
            nx, ny, nz = h+dx, r+dy, c+dz
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5\
            and visited[h][r][c]+1 < visited[nx][ny][nz] and arr[nx][ny][nz] == '1':
                visited[nx][ny][nz] = visited[h][r][c] + 1
                queue.append((nx,ny,nz))
    return visited[-1][-1][-1]

def rotate(n, arr3d):
    global answer
    if n == 5:
        for p in perm:
            answer = min(answer, bfs(list(map(lambda x: arr3d[x], p))))
            if answer == 13: return
        return

    new_arr3d = [[row[:] for row in arr2d] for arr2d in arr3d]
    rotate(n+1, new_arr3d)
    new_arr3d[n] = list(zip(*arr3d[n][::-1]))
    rotate(n+1, new_arr3d)
    new_arr3d[n] = list(zip(*arr3d[n]))[::-1]
    rotate(n+1, new_arr3d)
    new_arr3d[n] = [arr2d[::-1] for arr2d in arr3d[n][::-1]]
    rotate(n+1, new_arr3d)

def recur(arr):
    global perm
    if len(arr) == 5:
        perm.append(arr)
    for x in range(5):
        if not arr or x not in arr:
            recur(arr+[x])

arr3d = [[input().split() for _ in range(5)] for _ in range(5)]
answer = 126
perm = []
recur([])
rotate(0, arr3d)
print(-1 if answer == 126 else answer-1)