# TODO: 다시 풀어보기
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX86Fdm65RMDFAQe&probBoxId=AYncoPLaHscDFARi+&type=USER&problemBoxTitle=14_230810%3A+%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5_%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89&problemBoxCnt=++5+
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
arr = [0]
i = 1
for tc in range(1,T+1):
    N = int(input())
    while arr[-1] <= N:
        arr.append(i*i*i)
        i += 1
    try:
        print(f'#{tc} {arr.index(N)}')
    except:
        print(f'#{tc} {-1}')

# 이진 탐색으로 찾는 방법
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    start, end = 1, N
    answer = -1
    while start <= end:
        mid = (start+end)//2
        if mid**3 == N:   # m이 찾는 세제곱근인 경우
            answer = mid
            break
        elif mid**3 < N:
            start = mid+1
        else:
            end = mid-1
    print(f'#{tc} {answer}')