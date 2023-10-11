# https://www.acmicpc.net/problem/2933
from sys import stdin
stdin = open('input.txt')
input = stdin.readline

def down(x, y):
    # 덩어리와 바닥 저장해두기
    mineral = [[] for _ in range(C)]
    mineral[y].append(x)
    bottom = [None]*C
    bottom[y] = x

    # 덩어리 찾기
    visited = [[False]*C for _ in range(R)]
    visited[x][y] = True
    stack = [(x,y)]
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and matrix[nx][ny] == 'x':
                visited[nx][ny] = True
                stack.append((nx,ny))
                mineral[ny].append(nx)
                if bottom[ny]:
                    bottom[ny] = max(nx, bottom[ny])
                else:
                    bottom[ny] = nx

    # 어디까지 내릴 수 있는지 찾기
    mn = R
    for c, r in enumerate(bottom):
        if r is None: continue
        if r == R-1: return
        for i in range(1,R-1):
            if r+i < R and matrix[r+i][c] == '.': continue
            else:
                mn = min(i-1, mn)

    # 내리기
    for c in range(C):
        if not mineral[c]: continue
        for r in sorted(mineral[c], reverse=True):
            matrix[r+mn][c], matrix[r][c] = matrix[r][c], matrix[r+mn][c]

# 던지기
def destroy(x, left):
    if left:
        for c in range(C):
            if matrix[R-x][c] == 'x':
                matrix[R-x][c] = '.'
                for dx, dy in ((1,0),(0,1),(-1,0)):
                    nx, ny = R-x+dx, c+dy
                    if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == 'x':
                        down(nx, ny)
                return
    else:
        for c in range(C-1,-1,-1):
            if matrix[R-x][c] == 'x':
                matrix[R-x][c] = '.'
                for dx, dy in ((1,0),(0,-1),(-1,0)):
                    nx, ny = R-x+dx, c+dy
                    if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == 'x':
                        down(nx, ny)
                return

R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]
N = int(input())
arr = list(map(int, input().split()))

left = 1
for x in arr:
    destroy(x, left)
    left ^= 1
for row in matrix:
    print(''.join(row))