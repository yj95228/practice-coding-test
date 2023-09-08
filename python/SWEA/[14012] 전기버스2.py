# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9KHOLaJYYDFAQe&probBoxId=AYoFrWv6OdQDFARi+&type=USER&problemBoxTitle=19_230818%3A+%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C_Test_04&problemBoxCnt=++3+
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]
    answer, i = 0, 0
    while True:
        charge = arr[i]
        if i+charge+1 >= N: break
        mx, mx_idx = 0, 0
        for idx,x in enumerate(arr[i+1:i+charge+1], start=1):
            if mx < idx+x: mx, mx_idx = idx+x, idx
        i += mx_idx
        answer += 1
    print(f'#{tc} {answer}')