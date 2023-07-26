# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7wrjAKSucDFARO&probBoxId=AYmPVHzKcGEDFARi&type=USER&problemBoxTitle=03_230726&problemBoxCnt=5
import sys
sys.stdin=open("input.txt","rt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sm = sum([sum(row[j:j+M]) for row in arr[i:i+M]])
            answer = max(answer, sm)
    print(f'#{tc} {answer}')