# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYKBBpkqXJ8DFAVG&probBoxId=AYmCURrqky0DFAUe&type=USER&problemBoxTitle=02_230725&problemBoxCnt=6
import sys
sys.stdin=open("python\SWEA\input.txt","rt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # print(f'#{tc} {max(list(len, input().split('0')))}')
    answer = mx = 0
    for x in list(input()):
        if x == '1':
            mx += 1
            answer = max(answer, mx)
        else:
            mx = 0
    print(f'#{tc} {answer}')