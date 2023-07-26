# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7iAKtammUDFAS2&probBoxId=AYmCURrqky0DFAUe&type=USER&problemBoxTitle=02_230725&problemBoxCnt=6
import sys
sys.stdin=open("input.txt","rt")
T = int(input())

def solution(N, arr):
    half = N // 2  # 5이면 2
    answer = 0
    for x in range(half):
        answer += sum(arr[x][half-x:half+x+1])
    for x in range(half,N):
        answer += sum(arr[x][half-N+x+1:half+N-x])

    # 강사님 코드
    # arr = [input() for _ in range(N)]
    # for r in range(N):
    #     begin = abs(half-r)
    #     for c in range(begin, N-begin):
    #         answer += ord(arr[r][c]) - ord('0')
    return answer

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    print(f'#{tc} {solution(N, arr)}')