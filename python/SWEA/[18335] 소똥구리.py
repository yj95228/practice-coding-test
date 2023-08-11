# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AYnfeR1qU5YDFAU6&solveclubId=AYmCPbwakowDFAUe&problemBoxTitle=15_230811%3A+greedy_Test_03&problemBoxCnt=4&probBoxId=AYnhsQg60D4DFARi+
import sys
sys.stdin = open('input.txt','r')
T = int(input())

def dfs(idx, cnt, result):
    global answer
    answer = max(result, answer)
    if cnt >= M or idx >= N: return
    if idx+1 < N: dfs(idx+1, cnt+1, result+arr[idx+1])
    if idx+2 < N: dfs(idx+2, cnt+1, result//2+arr[idx+2])

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0
    dfs(-1, 0, 1)
    print(f'#{tc} {answer}')