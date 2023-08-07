# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq
import sys

sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    if N%2: matrix[N//2][N//2] = N*N
    def solution(N,i,j):
        if N <= 1: return
        for x in range(N-1):
            matrix[0+j][x+j] = i
            i += 1
        for x in range(N-1):
            matrix[x+j][N-1+j] = i
            i += 1
        for x in range(N-1):
            matrix[N-1+j][N-x-1+j] = i
            i += 1
        for x in range(N-1):
            matrix[N-x-1+j][0+j] = i
            i += 1
        return solution(N-2, i, j+1)
    solution(N, 1, 0)
    print(f'#{tc}')
    for m in matrix:
        print(*m)

# 두번째 풀이
def dfs(r,c,num,d):
    if num > N*N: return
    matrix[r][c] = num
    if 0 <= r+dx[d] < N and 0 <= c+dy[d] < N\
    and matrix[r+dx[d]][c+dy[d]] == 0:
        dfs(r+dx[d], c+dy[d], num+1, d)
    else:
        dfs(r+dx[(d+1)%4], c+dy[(d+1)%4], num+1, (d+1)%4)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    dfs(0,0,1,0)
    print(f'#{tc}')
    for m in matrix:
        print(*m)