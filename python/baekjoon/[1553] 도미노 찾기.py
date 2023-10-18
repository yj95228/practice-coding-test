# https://www.acmicpc.net/problem/1553
from sys import stdin
input = stdin.readline

def find_index(visited):
    for r in range(8):
        for c in range(7):
            if not visited[r][c]:
                return r, c

def recur(n, dominos, visited):
    global answer
    if n == 28:
        answer += 1
        return
    r, c = find_index(visited)
    if r+1 < 8 and not visited[r][c] and not visited[r+1][c]:
        for i in range(28):
            if dominos[i]: continue
            if domino[i] == (A[r][c], A[r+1][c]) or domino[i] == (A[r+1][c], A[r][c]):
                dominos[i], visited[r][c], visited[r+1][c] = 1, 1, 1
                recur(n+1, dominos, visited)
                dominos[i], visited[r][c], visited[r+1][c] = 0, 0, 0
    if c+1 < 7 and not visited[r][c] and not visited[r][c+1]:
        for i in range(28):
            if dominos[i]: continue
            if domino[i] == (A[r][c], A[r][c+1]) or domino[i] == (A[r][c+1], A[r][c]):
                dominos[i], visited[r][c], visited[r][c+1] = 1, 1, 1
                recur(n+1, dominos, visited)
                dominos[i], visited[r][c], visited[r][c+1] = 0, 0, 0

domino = []
for i in range(7):
    for j in range(i, 7):
        domino.append((i,j))
A = [list(map(int, input().rstrip())) for _ in range(8)]
visited = [[0]*7 for _ in range(8)]
answer = 0
recur(0, [0]*28, visited)
print(answer)