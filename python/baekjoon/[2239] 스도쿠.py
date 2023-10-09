# https://www.acmicpc.net/problem/2239
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def recur(n, matrix):
    global answer
    if answer: return
    narr = [row[:] for row in matrix]
    if n == length:
        answer = narr
        return
    visited = [False]*10
    x, y = blank[n]
    for r in range(9):
        visited[narr[r][y]] = True
    for c in range(9):
        visited[narr[x][c]] = True
    for r in range(3):
        for c in range(3):
            visited[narr[x//3*3+r][y//3*3+c]] = True
    for v in range(1,10):
        if not visited[v]:
            narr[x][y] = v
            recur(n+1, narr)
            narr[x][y] = 0

matrix = [list(map(int, list(input().rstrip()))) for _ in range(9)]
blank = []
for r in range(9):
    for c in range(9):
        if matrix[r][c] == 0:
            blank.append((r,c))
length = len(blank)
answer = None
recur(0, matrix)
for row in answer:
    print(''.join(map(str,row)))