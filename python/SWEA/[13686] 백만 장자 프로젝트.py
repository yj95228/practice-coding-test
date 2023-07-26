# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7w9f1KTFIDFARO&probBoxId=AYmCURrqky0DFAUe&type=USER&problemBoxTitle=02_230725&problemBoxCnt=6
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    while len(arr):
        mx = max(arr)
        idx = arr.index(mx)
        answer += mx*idx - sum(arr[:idx])
        arr = arr[idx+1:]
    print(f'#{tc} {answer}')