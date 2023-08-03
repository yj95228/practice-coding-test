# https://www.acmicpc.net/problem/2178
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
distance = [[0]*M for _ in range(N)]
queue = [(0,0)]
while queue:
    r, c = queue.pop(0)
    if r == N-1 and c == M-1: break
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if 0 <= r+dx < N and 0 <= c+dy < M and\
        not distance[r+dx][c+dy] and matrix[r+dx][c+dy] == '1':
            distance[r+dx][c+dy] = distance[r][c] + 1
            queue.append((r+dx, c+dy))
print(distance[r][c]+1)