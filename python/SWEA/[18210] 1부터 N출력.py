# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnIy86qE3wDFAUe&probBoxId=AYnNE126270DFARi&type=USER&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11
import sys

def solve(x):
    arr[x-1] = x
    return arr if x == 1 else solve(x-1)
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [1]*N
    print(f'#{tc}',*solve(N))

# 다른 사람 풀이 (1) solve(N)
def solve(x):
    if x == 1:
        return [1]
    return solve(x-1) + [x]

# 다른 사람 풀이 (2) solve(1)
def solve(x):
    # [0] 종료조건 (가능하다면 N으로 관련된 것으로)
    if x > N:
        return
    # [1] 단위작업 (순서는 바뀔 수 있음)
    print(x, end=' ')
    # [2] 하부호출(재귀호출) : N이 변화할수록 호출해야함 (종료조건 방향으로)
    solve(x+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [1]*N
    print(f'#{tc}', end=' ')
    solve(1)
    print()