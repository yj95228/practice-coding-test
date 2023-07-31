# https://www.acmicpc.net/problem/1018
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
arrW = [[0]*M for _ in range(N)]
arrB = [[0]*M for _ in range(N)]
startW, startB = 0, 0
answer = N*M
for r in range(N):
    for c in range(M):
        if (r+c)%2 == 0 and matrix[r][c] == 'W': arrB[r][c] = 1
        if (r+c)%2 == 0 and matrix[r][c] == 'B': arrW[r][c] = 1
        if (r+c)%2 == 1 and matrix[r][c] == 'W': arrW[r][c] = 1
        if (r+c)%2 == 1 and matrix[r][c] == 'B': arrB[r][c] = 1
for r in range(N-8+1):
    for c in range(M-8+1):
        answer = min(answer, sum([sum(row[c:c+8]) for row in arrB[r:r+8]]), sum([sum(row[c:c+8]) for row in arrW[r:r+8]]))
print(answer)

# 두번째 풀이
min_b, min_w = 64, 64
for r in range(N-8+1):
    for c in range(M-8+1):
        b, w = 0, 0
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0 and matrix[r+i][c+j] != 'W': w += 1
                elif (i+j)%2 == 0 and matrix[r+i][c+j] != 'B': b += 1
                elif (i+j)%2 == 1 and matrix[r+i][c+j] != 'B': w += 1
                elif (i+j)%2 == 1 and matrix[r+i][c+j] != 'W': b += 1
        min_b = min(min_b, b)
        min_w = min(min_w, w)
print(min(min_b, min_w))