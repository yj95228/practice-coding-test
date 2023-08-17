# https://www.acmicpc.net/problem/8911
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

T = int(input())
dir = [(-1,0),(0,1),(1,0),(0,-1)]
for _ in range(T):
    r, c, minr, minc, maxr, maxc, direction = 0, 0, 0, 0, 0, 0, 0
    for comm in list(input().rstrip()):
        if comm == 'F':
            dx, dy = dir[direction]
            r, c = r+dx, c+dy
        elif comm == 'B':
            dx, dy = dir[direction]
            r, c = r-dx, c-dy
        elif comm == 'L':
            direction = (direction-1)%4
        else:
            direction = (direction+1)%4
        minr, minc = min(minr, r), min(minc, c)
        maxr, maxc = max(maxr, r), max(maxc, c)
    print((maxr-minr)*(maxc-minc))