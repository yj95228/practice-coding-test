# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7tKT1qCH0DFARO&probBoxId=AYmPVHzKcGEDFARi&type=USER&problemBoxTitle=03_230726&problemBoxCnt=5
import sys
sys.stdin=open("input.txt","rt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                arr[r][c] += 1 if color == 1 else 2
    answer = sum([x == 3 for row in arr for x in row])
    print(f'#{tc} {answer}')