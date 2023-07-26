# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7YBpzKdxMDFAS2&probBoxId=AYmCURrqky0DFAUe&type=USER&problemBoxTitle=02_230725&problemBoxCnt=6
import sys
sys.stdin=open("python\SWEA\input.txt","rt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = [0]*10
    lst = map(int, list(input()))
    for x in lst:
        cnt[x] += 1
    idx  = 0
    for i in range(10):
        if cnt[i] >= cnt[idx]:
            idx = i
    print(f'#{tc} {idx} {cnt[idx]}')