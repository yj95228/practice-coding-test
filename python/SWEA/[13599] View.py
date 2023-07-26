# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7dEaBqfOUDFAS2&probBoxId=AYmCURrqky0DFAUe+&type=USER&problemBoxTitle=02_230725&problemBoxCnt=++6+
import sys

sys.stdin = open("input.txt", "rt")
for tc in range(10):
    N = int(input())
    answer = 0
    arr = list(map(int, input().split()))
    K = 2
    for i in range(K, len(arr) - K):
        mx = arr[i - K]
        for j in range(i - K + 1, i + K + 1):
            if i == j: continue
            mx = max(mx, arr[j])
        if arr[i] > mx:
            answer += arr[i] - mx
    print(f'#{tc + 1} {answer}')
