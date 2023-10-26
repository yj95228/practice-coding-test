# https://www.acmicpc.net/problem/4991
from sys import stdin
from collections import deque
stdin = open('input.txt','r')
input = stdin.readline

def bfs(i, j):
    (sr, sc), (er, ec) = dirty[i], dirty[j]
    queue = deque([(0, sr, sc)])
    V = [[0]*(W+2) for _ in range(H+2)]
    V[sr][sc] = 1
    while queue:
        time, r, c = queue.popleft()
        if (r, c) == (er, ec):
            D[i][j] = time
            D[j][i] = time
        else:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if not V[nx][ny] and A[nx][ny] != 'x':
                    V[nx][ny] = 1
                    queue.append((time+1, nx, ny))
    return -1

def recur(n, current, result):
    global answer
    if result > answer: return
    if n == length-1:
        answer = min(answer, result)
    for x in range(1, length):
        if visited[x]: continue
        visited[x] = 1
        dist = D[current][x]
        if dist: recur(n+1, x, result+dist)
        else: return
        visited[x] = 0

while True:
    W, H = map(int, input().split())
    if (W, H) == (0, 0): break
    A = [['x']*(W+2)] + [['x'] + list(input().rstrip()) + ['x'] for _ in range(H)] + [['x']*(W+2)]
    dirty, sr, sc = [], None, None
    for r in range(1, H+1):
        for c in range(1, W+1):
            if A[r][c] == 'o':
                A[r][c] = '.'
                sr, sc = r, c
            elif A[r][c] == '*':
                dirty.append((r, c))
    dirty.insert(0, (sr, sc))
    length = len(dirty)
    D = [[0]*length for _ in range(length)]
    for i in range(length-1):
        for j in range(i+1, length):
            bfs(i, j)

    answer = 987654321
    visited = [0]*length
    visited[0] = 1
    recur(0, 0, 0)
    print(-1 if answer == 987654321 else answer)