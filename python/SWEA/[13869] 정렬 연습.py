# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8lV0nq4O8DFARO&probBoxId=AYmCPbwako0DFAUe&type=USER&problemBoxTitle=01_230724&problemBoxCnt=6
#import sys
#sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 메소드 없이 풀기
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         if arr[i] > arr[j]:
    #             arr[j], arr[i] = arr[i], arr[j]
    # print(f'#{tc} {" ".join(map(str, arr))}')
    print(f'#{tc} {" ".join(list(map(str, sorted(lst))))}')