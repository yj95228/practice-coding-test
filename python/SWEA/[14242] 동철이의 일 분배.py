# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX_Zgst6Ap8DFAVy&probBoxId=AYnXZtca8dEDFARi+&type=USER&problemBoxTitle=13_230809%3A+Backtracking_3&problemBoxCnt=3
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,rate):
    global answer
    if answer > rate: return
    if n == N:
        if answer < rate: answer = rate
        return
    for i in range(N):
        if not visited[i] and matrix[n][i]:
            visited[i] = True
            dfs(n + 1, rate * matrix[n][i])
            visited[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    answer = 0
    visited = [False]*N
    dfs(0,1)
    print(f'#{tc} {answer*100:.6f}')