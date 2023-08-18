# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX-0MvfKQQ4DFARi&probBoxId=AYoFrWv6OdQDFARi+&type=USER&problemBoxTitle=19_230818%3A+%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C_Test_04&problemBoxCnt=3
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    matrix = [[0]*N for _ in range(N)]
    matrix[N//2-1][N//2-1] = 2
    matrix[N//2][N//2-1] = 1
    matrix[N//2-1][N//2] = 1
    matrix[N//2][N//2] = 2
    answer = [0,0]
    for _ in range(M):
        R, C, S = map(int, input().split())
        r, c = R-1, C-1
        matrix[r][c] = S
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
            i = 1
            while 0 <= r+dx*i < N and 0 <= c+dy*i < N and matrix[r+i*dx][c+i*dy] > 0:
                if 0 <= r+(i+1)*dx < N and 0 <= c+(i+1)*dy < N and matrix[r+i*dx][c+i*dy] != S and matrix[r+(i+1)*dx][c+(i+1)*dy] == S:
                    while i > 0:
                        matrix[r+i*dx][c+i*dy] = S
                        i -= 1
                    break
                else:
                    i += 1
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1: answer[0] += 1
            else: answer[1] += 1
    print(f'#{tc}',*answer)