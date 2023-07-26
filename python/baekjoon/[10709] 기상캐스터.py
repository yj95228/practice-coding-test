# https://www.acmicpc.net/problem/10709
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
H, W = map(int, input().split())
matrix = [list(input()) for _ in range(H)]
for r in range(H):
    arr = []
    for c in range(W):
        if matrix[r][c] == 'c':
            arr.append(0)
        else:
            for i in range(1, W):
                if c-i >= 0 and matrix[r][c-i] == 'c':
                    arr.append(i)
                    break
            else:
                arr.append(-1)
    print(*arr)