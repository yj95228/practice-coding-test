# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYmXhjSqxvMDFAUe&probBoxId=AYmbEeqKCscDFARi&type=USER&problemBoxTitle=05_230728%3A+Test01&problemBoxCnt=3
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    # N : input 갯수, M : 찾을 국력의 합
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if arr[i]+arr[j]+arr[k] == M:
                    answer += 1
    print(f'#{tc} {answer}')