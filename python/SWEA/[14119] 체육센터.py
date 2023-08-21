# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX-u4j5KeBsDFARi&probBoxId=AYoWpgnai9cDFARi&type=USER&problemBoxTitle=20_230821%3A+%EC%97%B0%EC%8A%B5_01&problemBoxCnt=2
import sys
sys.stdin = open('input.txt', 'r')

def dfs(m, sm):
    global answer
    if sm > answer: return
    elif m >= 12:
        answer = min(answer, sm)
        return
    dfs(m+1, sm+day[m])
    dfs(m+1, sm+month[m])
    dfs(m+3, sm+money[2])

T = int(input())
for tc in range(1,T+1):
    money = list(map(int, input().split()))
    day = list(map(lambda x: int(x)*money[0], input().split()))
    month = list(map(lambda x: money[1] if x else 0, day))
    answer = money[-1]
    dfs(0,0)
    print(f'#{tc} {answer}')

# dp로 푸는 방법
T = int(input())
for tc in range(1,T+1):
    money = list(map(int, input().split()))
    day = [0] + list(map(int, input().split()))
    dp = [0]*13
    for i in range(1,13):
        dp[i] = dp[i-1] + day[i]*money[0]
        dp[i] = min(dp[i], dp[i-1]+money[1])
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3]+money[2])
    answer = min(money[-1], dp[12])
    print(f'#{tc} {answer}')