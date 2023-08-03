# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX805keq15EDFAQe&probBoxId=AYm4kJEa4c4DFARi&type=USER&problemBoxTitle=09_230803%3A+Queue_BFS&problemBoxCnt=5
import sys

def bfs(current):
    queue = [current]
    while queue:
        r, c = queue.pop(0)
        if matrix[r][c] == '3':
            return distance[r][c]-1
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            if 0 <= r+dx < N and 0 <= c+dy < N and\
            not distance[r+dx][c+dy] and matrix[r+dx][c+dy] != '1':
                queue.append((r+dx, c+dy))
                distance[r+dx][c+dy] = distance[r][c] + 1

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    distance = [[0]*N for _ in range(N)]
    r, c = 0, 0
    for x in range(N):
        line = list(input())
        matrix.append(line)
        if '2' in line:
            r, c = x, line.index('2')
    print(f'#{tc} {bfs((r,c)) or 0}')