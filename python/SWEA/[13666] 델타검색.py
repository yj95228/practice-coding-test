# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7tKT1qCH0DFARO&probBoxId=AYmPVHzKcGEDFARi&type=USER&problemBoxTitle=03_230726&problemBoxCnt=5
import sys
sys.stdin=open("input.txt","rt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            if r > 0: answer += abs(arr[r][c] - arr[r - 1][c])
            if r < N - 1: answer += abs(arr[r][c] - arr[r + 1][c])
            if c > 0: answer += abs(arr[r][c] - arr[r][c - 1])
            if c < N - 1: answer += abs(arr[r][c] - arr[r][c + 1])

            # 다른 방법
            # for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            #     if 0 <= r+dx < N and 0 <= r+dy < N:
            #         answer += abs(arr[r][c] - arr[r+dx][c+dy])
    print(f'#{tc} {answer}')