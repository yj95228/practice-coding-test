# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9DSN2KIoQDFAQe&probBoxId=AYncoPLaHscDFARi+&type=USER&problemBoxTitle=14_230810%3A+%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89&problemBoxCnt=++4+
import sys
sys.stdin = open('input.txt', 'r')

def divide_and_conquer(arr):
    if len(arr) <= 1: return arr[0]
    center = (len(arr)+1)//2
    left, right = divide_and_conquer(arr[:center]), divide_and_conquer(arr[center:])
    if (left[1] == 1 and right[1] == 2)\
    or (left[1] == 2 and right[1] == 3)\
    or (left[1] == 3 and right[1] == 1):
        return right
    else: return left

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {divide_and_conquer(list(enumerate(arr)))[0]+1}')

# idx로 접근하는 방법
def win(start, end):
    # [1] 종료조건
    if start == end: return start
    # [2] left, right로 나눠서 각각의 승자 구하기
    mid = (start+end)//2
    left, right = win(start, mid), win(mid+1, end)
    # [3] 단위작업: left와 right의 승부를 판단
    return right if (arr[left]%3)+1 == arr[right] else left
