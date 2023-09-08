# https://www.acmicpc.net/problem/1932
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(1,N):
    for j in range(i+1):
        if j == 0: matrix[i][j] += matrix[i-1][j]
        elif j == i: matrix[i][j] += matrix[i-1][j-1]
        else: matrix[i][j] += max(matrix[i-1][j-1], matrix[i-1][j])
print(max(matrix[-1]))