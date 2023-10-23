# https://www.acmicpc.net/problem/3019
from sys import stdin
input = stdin.readline

C, P = map(int, input().split())
arr = list(map(int, input().split()))
dt = ((-3,0),
      (-2,0),(-2,1),
      (-1,0),(-1,1),(-1,2),
      (0,0),(0,1),(0,2),(0,3),
      (1,0),(1,1),(1,2),
      (2,0),(2,1))
'''
0
1 2
3 4 5
6 7 8 9
0 1 2
3 4
'''
tetris = [
    [],
    [[6,3,1,0],[9,8,7,6]],
    [[7,6,4,3]],
    [[7,6,5,4],[11,7,6,3]],
    [[12,11,7,6],[6,4,3,2]],
    [[8,7,6,4],[6,4,3,1],[11,8,7,6],[11,7,6,4]],
    [[8,7,6,5],[7,6,3,1],[6,5,4,3],[14,11,7,6]],
    [[8,7,6,3],[6,3,2,1],[12,8,7,6],[7,6,4,2]]
]
answer = 0
height = max(arr)+4
A = [[0]*C for _ in range(height)]
for c in range(C):
    for r in range(1,arr[c]+1):
        A[-r][c] = 1
for tt in tetris[P]:
    for c in range(C):
        tmp = []
        for t in tt:
            dx, dy = dt[t]
            nx, ny = height-arr[c]-1+dx, c+dy
            if 0 <= nx < height and 0 <= ny < C and not A[nx][ny] and\
                (nx+1 == height or (nx+1 < height and A[nx+1][ny])):
                A[nx][ny] = 1
                tmp.append((nx,ny))
            else: break
        else:
            answer += 1
        for r, c in tmp:
            A[r][c] = 0
print(answer)