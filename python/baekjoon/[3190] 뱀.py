# https://www.acmicpc.net/problem/3190
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
matrix = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 1
L = int(input())
arr = [input().split() for _ in range(L)]
info = {int(n) : dr for n, dr in arr}
answer, r, c, d = 0, 0, 0, 0
snake = [(r,c)]
direction = [(0,1),(1,0),(0,-1),(-1,0)]

while True:
    dx, dy = direction[d]
    r, c = snake[-1]
    answer += 1
    if 0 <= r+dx < N and 0 <= c+dy < N and (r+dx, c+dy) not in snake:
        snake.append((r+dx, c+dy))
        if matrix[r+dx][c+dy] == 0: snake.pop(0)
        else: matrix[r+dx][c+dy] = 0
        if answer in info:
            if info[answer] == 'L': d = (d-1)%4
            else: d = (d+1)%4
    else: break
print(answer)