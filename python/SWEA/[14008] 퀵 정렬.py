# TODO: 안보고 다시 짜보기
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9DSN2KIoQDFAQe&probBoxId=AYncoPLaHscDFARi+&type=USER&problemBoxTitle=14_230810%3A+%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89&problemBoxCnt=++4+
import sys
sys.stdin = open('input.txt', 'r')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    left, right = [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(arr)[N//2]}')