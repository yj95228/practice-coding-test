# TODO: (x,y) 좌표 다른 것 주의 / 규칙 찾기 어려웠음
# https://www.acmicpc.net/problem/15685
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
matrix = [[0]*101 for _ in range(101)]
dt = [(0,1),(-1,0),(0,-1),(1,0)]
for _ in range(N):
    X, Y, D, G = map(int, input().split())
    matrix[Y][X] = 1
    dy, dx = dt[D]
    matrix[Y+dy][X+dx] = 1

    arr = [(Y,X),(Y+dy,X+dx)]   # 점들의 위치
    rotate = [D]                # 회전할 방향

    for g in range(G):
        r = len(rotate)
        for i in range(r-1,-1,-1):
            y, x = arr[-1]
            d = rotate[i]
            dy, dx = dt[(d+1)%4]
            matrix[y+dy][x+dx] = 1
            arr.append((y+dy, x+dx))
            rotate.append((d+1)%4)
answer = 0
for r in range(100):
    for c in range(100):
        if matrix[r][c] and matrix[r+1][c] and matrix[r][c+1] and matrix[r+1][c+1]:
            answer += 1
print(answer)