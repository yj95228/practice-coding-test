# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnfWTGKUqkDFAU6&probBoxId=AYnhsQg60D4DFARi+&type=USER&problemBoxTitle=15_230811%3A+greedy_Test_03&problemBoxCnt=4
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    R, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    answer = 0
    matrix[R][C] = 2
    queue = [(R,C)]
    while queue:
        r, c = queue.pop(0)
        visited[r][c] = True
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0 <= r+dx < N and 0 <= c+dy < M and\
            not visited[r+dx][c+dy] and matrix[r+dx][c+dy] == 1:
                matrix[r+dx][c+dy] = matrix[r][c] + 1
                queue.append((r+dx, c+dy))
    print(f'#{tc} {max(map(max, matrix))-1} {sum([row.count(1) for row in matrix])}')