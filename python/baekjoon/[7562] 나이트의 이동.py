# https://www.acmicpc.net/problem/2178
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    I = int(input())
    R, C = map(int, input().split())
    X, Y = map(int, input().split())
    matrix = [[0]*I for _ in range(I)]
    distance = [[0]*I for _ in range(I)]
    queue = [(R,C)]
    while queue:
        r, c = queue.pop(0)
        if r == X and c == Y: break
        for dx, dy in ((-1,-2),(-2,-1),(-1,2),(-2,1),(1,-2),(2,-1),(1,2),(2,1)):
            if 0 <= r+dx < I and 0 <= c+dy < I and not distance[r+dx][c+dy]:
                distance[r+dx][c+dy] += distance[r][c] + 1
                queue.append((r+dx, c+dy))
    print(distance[X][Y])