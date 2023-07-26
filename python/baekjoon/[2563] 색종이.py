# https://www.acmicpc.net/problem/2563
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
matrix = [[0]*100 for _ in range(100)]
for _ in range(N):
    A, B = map(int, input().split())
    for i in range(10):
        for j in range(10):
            matrix[A+i][B+j] = 1
print(sum([x == 1 for row in matrix for x in row]))