# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9eTLmq5IgDFAQe&probBoxId=AYnSX2OKO2YDFARi&type=USER&problemBoxTitle=12_230808%3A+Backtracking_2&problemBoxCnt=4
import sys
sys.stdin = open('input.txt', 'r')

def dfs(arr, sm):
    global answer
    if answer < sm: return
    elif B <= sm < answer: answer = sm
    if len(arr) == N: return
    else:
        for i,x in enumerate(lst):
            if not arr or arr[-1] < i:
                dfs(arr+[i], sm+x)

T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    answer = N*B
    dfs([], 0)
    print(f'#{tc} {answer-B}')

# 강사님 코드
def dfs(n, sm):
    global answer
    if answer == 0: return
    if n == N:
        if sm >= B:
            answer = min(answer, sm-B)
            return
    else:
        dfs(n+1, sm+lst[n])
        dfs(n+1, sm)