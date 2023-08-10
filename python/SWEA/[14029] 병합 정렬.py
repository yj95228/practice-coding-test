# TODO: 다시 풀어보기
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9DSN2KIoQDFAQe&probBoxId=AYncoPLaHscDFARi+&type=USER&problemBoxTitle=14_230810%3A+%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89&problemBoxCnt=++4+
import sys
sys.stdin = open('input.txt', 'r')

def merge_sort(arr):
    global answer
    # [1] 종료 조건 => 더 이상 머지소트 진행할 수 없는 경우
    if len(arr) <= 1:
        return arr

    # [2] 하부 호출 : 절반을 나눠서 정렬함수 호출
    center = len(arr)//2
    left, right = merge_sort(arr[:center]), merge_sort(arr[center:])

    # [0] 정답 관련 처리 left[-1]: right[-1] => answer += 1
    if left[-1] > right[-1]:
        answer += 1

    # [3] 단위 작업(병합 작업)
    result = []
    l = r = 0
    # 비교할 대상이 있는 동안 비교해서 작은 값 추가
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 남은 숫자들(left와 right 중 하나는 비어있음)을 뒤에 붙여줌
    return result + left[l:] + right[r:]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    print(f'#{tc} {merge_sort(arr)[N//2]} {answer}')