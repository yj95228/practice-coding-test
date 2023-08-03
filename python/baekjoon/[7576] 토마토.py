# https://www.acmicpc.net/problem/7576
import sys
from collections import deque

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
M, N = map(int, input().split())
matrix, queue = [], deque()
visited = [[0]*M for _ in range(N)]
for r in range(N):
    line = tuple(input().split())
    matrix.append(line)
    if '1' in line or '-1' in line:
        for c in range(M):
            if line[c] == '1':
                queue.append((r,c))
                visited[r][c] = 1
            elif line[c] == '-1':
                visited[r][c] = 1
while queue:
    r, c = queue.popleft()
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        if 0 <= r+dx < N and 0 <= c+dy < M and\
        not visited[r+dx][c+dy] and matrix[r+dx][c+dy] == '0':
            visited[r+dx][c+dy] += visited[r][c] + 1
            queue.append((r+dx, c+dy))
def solve():
    answer = 0
    for r in range(N):
        for c in range(M):
            if visited[r][c] == 0: return -1
            else:
                answer = max(visited[r][c], answer)
    return answer-1
print(solve())