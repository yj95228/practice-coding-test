# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYKLSmf6S9UDFAVG&probBoxId=AYncoPLaHscDFARi+&type=USER&problemBoxTitle=14_230810%3A+%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89&problemBoxCnt=5
import sys
sys.stdin = open('input.txt', 'r')

def binary_search(start, end, d):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == d:
            return mid+1
        elif arr[mid] < d:
            start = mid+1
        else:
            end = mid-1
    return 0

T = int(input())
for tc in range(1,T+1):
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {binary_search(0, N-1, D)}')