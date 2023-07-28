# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYmXgn9qxq4DFAUe&probBoxId=AYmbEeqKCscDFARi&type=USER&problemBoxTitle=05_230728%3A+Test01&problemBoxCnt=3
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    # N : ??, K : 좌표 수(input 들어올 횟수), C : 색깔
    N, K, C = map(int, input().split())
    matrix = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(K):
        r, c, x, y, color = map(int, input().split())
        for i in range(x):
            for j in range(y):
                matrix[r+i-1][c+j-1] = color
    print(f'#{tc} {sum([x == C for row in matrix for x in row])}')