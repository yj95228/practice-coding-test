# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8jzEIKxDoDFARO&probBoxId=AYmzaMrKU4cDFARi&type=USER&problemBoxTitle=08_230802%3A+DFS&problemBoxCnt=4
import sys

def dfs(r, c):
    if miro[r][c] == '3': return 1
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if 0 <= r+dx < N and 0 <= c+dy < N and\
        not visited[r+dx][c+dy] and miro[r+dx][c+dy] != '1':
            visited[r][c] = True
            if dfs(r+dx, c+dy): return 1
    return 0

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = []
    c = 0
    for x in range(N):
        line = list(input())
        miro.append(line)
        if '2' in line:
            r, c = x, line.index('2')
    visited = [[False]*N for _ in range(N)]
    print(f'#{tc} {dfs(r, c)}')