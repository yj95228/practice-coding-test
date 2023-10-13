def check(arr):
    narr = [row[:] for row in A]
    if arr:
        for x in arr:
            r, c = wall[x]
            narr[r][c] = '.'
    groups = [[0]*N for _ in range(N)]
    group = 1
    for r in range(N):
        for c in range(N):
            if narr[r][c] == '.' and not groups[r][c]:
                if group == 2: return False
                groups[r][c] = group
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < N and not groups[nx][ny] and narr[nx][ny] == '.':
                            groups[nx][ny] = group
                            stack.append((nx, ny))
                group += 1
    return True

def recur(n, start, arr):
    global answer
    if check(arr):
        answer = min(answer, len(arr))
        return
    if n == length or len(arr) >= answer:
        return
    for i in range(start, length):
        recur(n+1, i+1, arr+[i])

N = int(input())
A = [list(input().rstrip()) for _ in range(N)]
wall = []
for r in range(N):
    for c in range(N):
        if A[r][c] == '#':
            wall.append((r,c))
length = len(wall)
answer = 7
recur(0, 0, [])
print(-1 if answer == 7 else answer)

# 두번째 방법
from sys import stdin
from collections import deque
from heapq import heappop, heappush
stdin = open('input.txt')
input = stdin.readline

def check(matrix):
    groups = [[0]*N for _ in range(N)]
    group = 1
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == '.' and not groups[r][c]:
                if group == 2: return False
                groups[r][c] = group
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < N and not groups[nx][ny] and matrix[nx][ny] == '.':
                            groups[nx][ny] = group
                            stack.append((nx, ny))
                group += 1
    return True

def recur(n, cnt, lm):
    if cnt == lm:
        return check(matrix)
    for i in range(n, length):
        r, c = wall[i]
        matrix[r][c] = '.'
        if recur(i+1, cnt+1, lm):
            return True
        matrix[r][c] = '#'

N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]
wall = []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == '#':
            wall.append((r, c))
length = len(wall)
for l in range(7):
    if recur(0, 0, l):
        print(l)
        break
else:
    print(-1)