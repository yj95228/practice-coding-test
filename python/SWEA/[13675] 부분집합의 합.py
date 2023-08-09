# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7wkzAKSpEDFARO&probBoxId=AYnSX2OKO2YDFARi&type=USER&problemBoxTitle=12_230808%3A+Backtracking_2&problemBoxCnt=4
# 12개 중 N개 고르는 조합
import sys
sys.stdin = open('input.txt', 'r')

def dfs(arr):
    if len(arr) == N:
        return 1 if sum(arr) == K else 0
    else:
        answer = 0
        for x in range(1,13):
            if not arr or arr[-1] < x:
                answer += dfs(arr+[x])
    return answer

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    print(f'#{tc} {dfs([])}')

# 강사님 코드
def dfs(n, start, sm):
    global answer
    if K < sm: return   # 가지치기
    if n == N:
        if sm == K: answer += 1
        return
    for x in range(start, 13):
        dfs(n+1, x+1, sm+x)
dfs(0,1,0)