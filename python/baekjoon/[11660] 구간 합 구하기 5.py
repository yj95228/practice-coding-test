# https://www.acmicpc.net/problem/11660
import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
for x in range(1,2*N+1):
    for i in range(1,x+1):
        if i > N or x-i > N: continue
        if i and x-i: matrix[i][x-i] -= matrix[i-1][x-i-1]
        if i: matrix[i][x-i] += matrix[i-1][x-i]
        if x-i: matrix[i][x-i] += matrix[i][x-i-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(matrix[x2][y2]-matrix[x1-1][y2]-matrix[x2][y1-1]+matrix[x1-1][y1-1])