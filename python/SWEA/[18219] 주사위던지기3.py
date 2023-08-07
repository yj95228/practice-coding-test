# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnI5Y86FFEDFAUe&probBoxId=AYnNE126270DFARi&type=USER&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11
import sys
sys.stdin = open('input.txt','r')

def dfs(arr):
    if len(arr) == N:
        if sum(arr) == M:
            print(*arr)
    else:
        for i in range(1,7):
            dfs(arr + [i])

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    print(f'#{tc}')
    dfs([])