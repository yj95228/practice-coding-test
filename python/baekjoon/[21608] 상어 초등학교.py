# https://www.acmicpc.net/problem/21608
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
matrix = [[None]*N for _ in range(N)]
like4list = {}
for i in range(N*N):
    idx, *arr = map(int, input().split())
    like4list[idx] = arr
    where_is_best = []
    for r in range(N):
        for c in range(N):
            if not matrix[r][c]:
                like, empty = 0, 0
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    if 0 <= r+dx < N and 0 <= c+dy < N:
                        if matrix[r+dx][c+dy] in arr: like += 1
                        elif not matrix[r+dx][c+dy]: empty += 1
                where_is_best.append((r, c, like, empty))
    where_is_best.sort(key=lambda x: (-x[2],-x[3],x[0],x[1]))
    matrix[where_is_best[0][0]][where_is_best[0][1]] = idx
answer = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            if 0 <= r+dx < N and 0 <= c+dy < N and matrix[r+dx][c+dy] in like4list.get(matrix[r][c]):
                cnt += 1
        if cnt: answer += 10**(cnt-1)
print(answer)