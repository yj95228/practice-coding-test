# https://www.acmicpc.net/problem/16924
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def check(r,c):
    i = 1
    wrong = False
    while True:
        if wrong: break
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0 <= r+dx*i < N and 0 <= c+dy*i < M and matrix[r+dx*i][c+dy*i] == '*': continue
            wrong = True
            break
        else:
            i += 1
    return i

def visit(r,c,s):
    visited[r][c] = True
    for i in range(1,s+1):
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            visited[r+dx*i][c+dy*i] = True

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
answer = []
for r in range(N):
    for c in range(M):
        if matrix[r][c] == '*':
            s = check(r,c)
            if s > 1:
                visit(r,c,s-1)
                while s > 1:
                    answer.append((r+1,c+1,s-1))
                    s -= 1
for r in range(N):
    for c in range(M):
        if not visited[r][c] and matrix[r][c] == '*':
            answer = -1
            break
if answer == -1:
    print(-1)
else:
    print(len(answer))
    for a in answer:
        print(*a)