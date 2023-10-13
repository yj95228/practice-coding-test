# https://www.acmicpc.net/problem/2115
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [[[0]*M for _ in range(N)] for _ in range(4)]
for r in range(N):
    for c in range(M):
        if A[r][c] == 'X':
            for d, (dx, dy) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == '.':
                    B[d][nx][ny] = 1

answer = 0
for d in [0, 2]:
    for r in range(1,N):
        can = False
        for c in range(1,M):
            if B[d][r][c]:
                if can:
                    can = False
                    answer += 1
                else:
                    can = True
            else: can = False

for d in [1, 3]:
    for c in range(1,M):
        can = False
        for r in range(1,N):
            if B[d][r][c]:
                if can:
                    can = False
                    answer += 1
                else:
                    can = True
            else: can = False

print(answer)