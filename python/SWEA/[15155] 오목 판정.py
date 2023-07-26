# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYLI_hUK4yADFASv&probBoxId=AYmPVHzKcGEDFARi&type=USER&problemBoxTitle=03_230726&problemBoxCnt=5
import sys

sys.stdin = open("input.txt", "rt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dx, dy = [1, 0, 1, -1], [0, 1, 1, 1]
    arr = [list(input()) for _ in range(N)]
    answer = False
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for i in range(4):
                    tmp = True
                    for x in range(1,5):
                        if 0 <= r + x * dx[i] < N and 0 <= c + x * dy[i] < N:
                            if arr[r + x * dx[i]][c + x * dy[i]] == '.':
                                tmp = False
                        else:
                            tmp = False
                    if tmp == True:
                        answer = True
                        break
            if answer == True: break
        if answer == True: break
    print(f'#{tc} {"YES" if answer else "NO"}')