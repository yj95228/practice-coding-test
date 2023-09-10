# https://www.acmicpc.net/problem/29733
import sys
input = sys.stdin.readline

R, C, H = map(int, input().split())
arr3d = [[list(input().rstrip()) for _ in range(R)] for _ in range(H)]
for h in range(H):
    for r in range(R):
        for c in range(C):
            if arr3d[h][r][c] == '*': continue
            result = 0
            direction = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),
                         (1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0),
                         (0,1,1),(0,1,-1),(0,-1,1),(0,-1,-1),
                         (1,0,1),(1,0,-1),(-1,0,1),(-1,0,-1),
                         (1,1,1),(-1,1,1),(1,-1,1),(1,1,-1),
                         (-1,-1,1),(-1,1,-1),(1,-1,-1),(-1,-1,-1))
            for dx,dy,dz in direction:
                nx,ny,nz = h+dx,r+dy,c+dz
                if 0 <= nx < H and 0 <= ny < R and 0 <= nz < C and arr3d[nx][ny][nz] == '*':
                    result += 1
            arr3d[h][r][c] = result%10
for matrix in arr3d:
    for row in matrix:
        print(''.join(map(str,row)))