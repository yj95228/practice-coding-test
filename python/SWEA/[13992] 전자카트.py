# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX86SZQK6WMDFAQe&probBoxId=AYnXZtca8dEDFARi&type=USER&problemBoxTitle=13_230809%3A+Backtracking_3&problemBoxCnt=3
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,r,sm):
    global answer
    if answer < sm: return
    if n == N and r == 0:
        if answer > sm: answer = sm
        return
    for c in range(N):
        if not visited[c] and matrix[r][c]:
            visited[c] = True
            dfs(n+1,c,sm+matrix[r][c])
            visited[c] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 100*10*10
    visited = [False]*N
    dfs(0,0,0)
    print(f'#{tc} {answer}')