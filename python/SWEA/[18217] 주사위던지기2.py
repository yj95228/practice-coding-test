# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AYnI3SpqE_MDFAUe&solveclubId=AYmCPbwakowDFAUe&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11&probBoxId=AYnNE126270DFARi
import sys
sys.stdin = open('input.txt','r')

def dfs(arr):
    if len(arr) == N:
        print(*arr)
    else:
        for i in range(1,7):
            if not arr or arr[-1] <= i:
                dfs(arr+[i])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    dfs([])