# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYLTMmoKFBgDFASv&probBoxId=AYmCURrqky0DFAUe&type=USER&problemBoxTitle=02_230725&problemBoxCnt=6
from math import inf
import sys
sys.stdin=open("python\SWEA\input.txt","rt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    answer = -float(inf)
    if N > M:
        N, M = M, N
        arrA, arrB = arrB, arrA
    for i in range(0, M-N+1):
        tmp = 0
        newA = [0]*i + arrA + [0]*(M-N-i)
        for idx in range(M):
            tmp += newA[idx]*arrB[idx]
        if answer < tmp:
            answer = tmp
    print(f'#{tc} {answer}')