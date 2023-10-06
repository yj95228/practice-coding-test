# https://www.acmicpc.net/problem/2669
from sys import stdin
input = stdin.readline

matrix = [[0]*101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(x1,x2):
        for c in range(y1,y2):
            matrix[r][c] = 1
print(sum([matrix[r][c] for r in range(1,101) for c in range(1,101)]))