# https://www.acmicpc.net/problem/2468
import sys

def dfs(r, c):
    visited[r][c] = 1
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if 0 <= r + dx < N and 0 <= c + dy < N and\
        not visited[r+dx][c+dy] and matrix[r+dx][c+dy] >= x:
            dfs(r+dx, c+dy)

    # 메모리 부족 시 활용 -> 시간은 늘어남
    # ni = ci - 1
    # if 0 <= ni and v[ni][cj] == 0 and arr[ni][cj] > h:
    #     dfs(ni, cj, h)  # 상
    # ni = ci + 1
    # if ni < N and v[ni][cj] == 0 and arr[ni][cj] > h:
    #     dfs(ni, cj, h)  # 하
    # nj = cj - 1
    # if 0 <= nj and v[ci][nj] == 0 and arr[ci][nj] > h:
    #     dfs(ci, nj, h)  # 좌
    # nj = cj + 1
    # if nj < N and v[ci][nj] == 0 and arr[ci][nj] > h:
    #     dfs(ci, nj, h)  # 우

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