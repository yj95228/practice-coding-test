# https://www.acmicpc.net/problem/14712
from sys import stdin
input = stdin.readline

def recur(n):
    global answer
    if n == N*M:
        answer += 1
        return
    r, c = n//M, n%M
    recur(n+1)
    if not (0 <= r-1 and 0 <= c-1 and A[r-1][c-1] and A[r-1][c] and A[r][c-1]):
        A[r][c] = 1
        recur(n+1)
        A[r][c] = 0

N, M = map(int, input().split())
A = [[0]*M for _ in range(N)]
answer = 0
recur(0)
print(answer)