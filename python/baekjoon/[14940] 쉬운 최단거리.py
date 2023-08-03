# https://www.acmicpc.net/problem/14940
import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
visited = [[0]*M for _ in range(N)]
for x in range(N):
    line = list(map(lambda x: -1 if x == '1' else int(x), input().split()))
    matrix.append(line)
    if 2 in line:
        R, C = x, line.index(2)
queue = [(R,C)]
matrix[R][C] = 0
while queue:
    r, c = queue.pop(0)
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        if 0 <= r+dx < N and 0 <= c+dy < M and\
        not visited[r+dx][c+dy] and matrix[r+dx][c+dy] == -1:
            matrix[r+dx][c+dy] = matrix[r][c] + 1
            queue.append((r+dx, c+dy))
for row in matrix:
    print(*row)