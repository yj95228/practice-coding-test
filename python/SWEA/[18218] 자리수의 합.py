# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AYnI3SpqE_MDFAUe&solveclubId=AYmCPbwakowDFAUe&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11&probBoxId=AYnNE126270DFARi
import sys
sys.stdin = open('input.txt','r')

def dfs(x):
    return arr[x]+dfs(x+1) if x < len(arr) else 0

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, list(input())))
    print(f'#{tc} {dfs(0)}')

# 재귀로 10으로 나눈 나머지를 더하는 방법
def dfs(n):
    return 0 if n == 0 else n % 10 + dfs(n // 10)

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc} {dfs(int(input()))}')