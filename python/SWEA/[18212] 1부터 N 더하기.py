# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnIy86qE3wDFAUe&probBoxId=AYnNE126270DFARi&type=USER&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11
import sys

def solve(x):
    arr[x-1] = x
    return sum(arr) if x == 1 else solve(x-1)
    # return 1 if x == 1 else solve(x-1)+x
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0]*N
    print(f'#{tc} {solve(N)}')

# 1...n까지의 합을 하부함수로 전달, 종료 시 answer에 저장
def solve2(x, sm):
    global answer
    if x > N:
        answer = sm
        return
    # 하부 함수 호출
    solve2(x+1, sm+x)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    answer = 0
    print(f'#{tc} {solve(N)}')

    # solve2(1, 0)
    # print(f'#{tc} {answer}')