# https://www.acmicpc.net/problem/2583
import sys

def dfs(r,c):
    global result
    visited[r][c] = 1
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if 0 <= r+dx < M and 0 <= c+dy < N and\
        not visited[r+dx][c+dy] and matrix[r+dx][c+dy] == 1:
            result += 1
            dfs(r+dx, c+dy)

sys.setrecursionlimit(10000)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

M, N, K = map(int, input().split())
matrix = [[1]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
answer = []
for _ in range(K):
    B, A, Y, X = map(int, input().split())
    for r in range(A,X):
        for c in range(B,Y):
            matrix[r][c] = 0
for r in range(M):
    for c in range(N):
        result = 1
        if not visited[r][c] and matrix[r][c] == 1:
            dfs(r,c)
            answer.append(result)
print(len(answer))
print(*sorted(answer))