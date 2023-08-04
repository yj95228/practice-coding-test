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