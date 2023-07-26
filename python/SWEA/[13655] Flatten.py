# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7iAKtammUDFAS2&probBoxId=AYmCURrqky0DFAUe&type=USER&problemBoxTitle=02_230725&problemBoxCnt=6
import sys
sys.stdin=open("input.txt","rt")
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = min(100, max(arr)-min(arr))
    for _ in range(N):
        arr[arr.index(min(arr))] += 1
        arr[arr.index(max(arr))] -= 1
        answer = min(answer, max(arr)-min(arr))
    print(f'#{tc} {answer}')