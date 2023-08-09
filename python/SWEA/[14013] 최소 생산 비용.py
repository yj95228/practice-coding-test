# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9KIrOqJcUDFAQe&probBoxId=AYnSX2OKO2YDFARi&type=USER&problemBoxTitle=12_230808%3A+Backtracking_2&problemBoxCnt=4
# N개 중 N개 순열
import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, sm, arr):
    global answer
    if r == N:
        if sm < answer: answer = sm
    else:
        if sm < answer:
            for i in range(N):
                if not arr or i not in arr:
                    dfs(r+1, sm+matrix[r][i], arr+[i])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 15*15*99
    dfs(0, 0, [])
    print(f'#{tc} {answer}')

# 강사님 코드
def dfs(n, sm):
    global answer
    if answer <= sm: return
    if n == N:
        answer = min(answer, sm)
        return
    for j in range(N):
        if not visited[j]:
            visited[j] = True
            dfs(n+1, sm+matrix[n][j])
            visited[j] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 15 * 15 * 99
    visited = [0]*N
    dfs(0, 0)
    print(f'#{tc} {answer}')
