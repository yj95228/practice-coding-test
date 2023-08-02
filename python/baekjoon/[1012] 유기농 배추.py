# https://www.acmicpc.net/problem/1012
import sys

sys.setrecursionlimit(10000)
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def dfs(r, c):
    visited[r][c] = True
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= r + dx < N and 0 <= c + dy < M and \
        not visited[r + dx][c + dy] and matrix[r + dx][c + dy] == 1:
            dfs(r + dx, c + dy)
            matrix[r + dx][c + dy] = 0
    return 1    # 이거 안하고

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    answer = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 1:
                answer += dfs(r, c)
                # answer += 1 이렇게 푸는게 나았을지도
    print(answer)