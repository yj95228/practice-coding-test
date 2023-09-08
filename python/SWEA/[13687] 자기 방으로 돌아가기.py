# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7w_SUaTJMDFARO&probBoxId=AYoFrWv6OdQDFARi+&type=USER&problemBoxTitle=19_230818%3A+%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C_Test_04&problemBoxCnt=3
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = [0]*200
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        if A < B:
            for i in range((A-1)//2,(B-1)//2+1):
                arr[i] += 1
        else:
            for i in range((B-1)//2,(A-1)//2+1):
                arr[i] += 1
    print(arr)
    print(f'#{tc} {max(arr)}')