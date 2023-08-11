# TODO: 다시 풀어보기
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnXcFtK8eoDFARi&probBoxId=AYnXZtca8dEDFARi&type=USER&problemBoxTitle=13_230809%3A+Backtracking_3&problemBoxCnt=3
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, start, score, calory):
    global answer
    if calory > L: return   # 칼로리가 초과되면 아예 return시켜버려서 잘못된 코드
    if n == N: return
    if answer < score: answer = score
    for i in range(start, N):
        dfs(n+1, i+1, score+arr[i][0], calory+arr[i][1])

T = int(input())
for tc in range(1,T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    dfs(0, 0, 0, 0)
    print(f'#{tc} {answer}')

# 강사님 코드
def dfs(n, calory, sm):
    global answer
    if n == N:
        if calory < L:
            answer = max(answer, sm)
        return
    dfs(n+1, calory+arr[n][1], sm+arr[n][0])
    dfs(n+1, calory, sm)

T = int(input())
for tc in range(1,T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    dfs(0, 0, 0)
    print(f'#{tc} {answer}')