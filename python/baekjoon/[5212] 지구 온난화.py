# https://www.acmicpc.net/problem/5212
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]
sea_list = []
for r in range(R):
    for c in range(C):
        if matrix[r][c] == 'X':
            sea = 0
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if not (0 <= nx < R and 0 <= ny < C)\
                or (0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == '.'):
                    sea += 1
                    if sea >= 3:
                        sea_list.append((r,c))
                        break
if sea_list:
    for r,c in sea_list:
        matrix[r][c] = '.'

r_mn, r_mx, c_mn, c_mx = R, 0, C, 0
for r in range(R):
    for c in range(C):
        if matrix[r][c] == 'X':
            r_mn = min(r, r_mn)
            r_mx = max(r, r_mx)
            c_mn = min(c, c_mn)
            c_mx = max(c, c_mx)
for row in matrix[r_mn:r_mx+1]:
    print(''.join(row[c_mn:c_mx+1]))