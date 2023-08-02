# https://www.acmicpc.net/problem/2468
import sys

def dfs(r, c):
    visited[r][c] = 1
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if 0 <= r + dx < N and 0 <= c + dy < N and\
        not visited[r+dx][c+dy] and matrix[r+dx][c+dy] >= x:
            dfs(r+dx, c+dy)

sys.stdin = open('input.txt','rt')
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
answer = [1]
matrix = []
s = set()
for _ in range(N):
    line = tuple(map(int, input().split()))
    matrix.append(line)
    s.update(line)
s = sorted(s, reverse=True)
s.pop()
for x in s:
    visited = [[0] * N for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] >= x and not visited[r][c]:
                dfs(r, c)
                result += 1
    answer.append(result)
print(max(answer))