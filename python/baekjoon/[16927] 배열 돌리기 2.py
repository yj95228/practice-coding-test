# https://www.acmicpc.net/problem/16927
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, R = map(int, input().split())
matrix = [input().split() for _ in range(N)]
L = min(N//2, M//2)
for i in range(L):
    arr = deque([])
    for j in range(i,M-i):
        arr.append(matrix[i][j])
    for j in range(i+1, N-i-1):
        arr.append(matrix[j][M-i-1])
    for j in range(M-i-1,i-1,-1):
        arr.append(matrix[N-i-1][j])
    for j in range(N-i-1,i+1,-1):
        arr.append(matrix[j-1][i])
    arr.rotate(-R%len(arr))
    for j in range(i,M-i):
        matrix[i][j] = arr.popleft()
    for j in range(i+1, N-i-1):
        matrix[j][M-i-1] = arr.popleft()
    for j in range(M-i-1,i-1,-1):
        matrix[N-i-1][j] = arr.popleft()
    for j in range(N-i-1,i+1,-1):
        matrix[j-1][i] = arr.popleft()
for row in matrix:
    print(*row)