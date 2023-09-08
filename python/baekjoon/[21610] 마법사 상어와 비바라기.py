# https://www.acmicpc.net/problem/21610
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# [1] 비구름 생성
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
for _ in range(M):
    D, S = map(int, input().split())
    dt = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

    # [2] 이동
    cloud = list(map(lambda x: [(x[0]+S*dt[D-1][0])%N, (x[1]+S*dt[D-1][1])%N], cloud))

    # [3] 비 내리기
    visited = [[False]*N for _ in range(N)]
    for r,c in cloud:
        matrix[r][c] += 1
        visited[r][c] = True

    # [4] 물 복사
    for r,c in cloud:
        rain = 0
        for dx, dy in ((1,1),(-1,-1),(1,-1),(-1,1)):
            if 0 <= r+dx < N and 0 <= c+dy < N and matrix[r+dx][c+dy]:
                rain += 1
        matrix[r][c] += rain

    # [5] 구름 만들기
    new_cloud = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] >= 2 and not visited[r][c]:
                matrix[r][c] -= 2
                new_cloud.append([r,c])
    cloud = new_cloud

print(sum(sum(matrix,[])))