# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7YAPSadp0DFAS2&probBoxId=AYmCPbwako0DFAUe&type=USER&problemBoxTitle=01_230724&problemBoxCnt=6
#import sys
#sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    mn, mx = 10000*M, 0
    # for i in range(N-M+1):
    #     v = sum(lst[i:i+M])
    #     mn = min(v, mn)
    #     mx = max(v, mx)
    sm = sum(lst[:M])
    for i in range(1, N-M+1):
        sm -= lst[i]
        sm += lst[i+M]
        mn = min(mn, sm)
        mx = max(mx, sm)
    print(f'#{tc} {mx-mn}')