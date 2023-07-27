# https://www.acmicpc.net/problem/2567
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
answer = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] == 0:
            continue
        else:
            cross = 4
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                if 0 <= i+dx < 100 and 0 <= j+dy < 100 and matrix[i+dx][j+dy] == 0:
                    cross -= 1
            answer += cross
print(answer)