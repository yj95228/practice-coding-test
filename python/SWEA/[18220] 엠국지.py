# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnI6Ju6FF0DFAUe&probBoxId=AYnNE126270DFARi&type=USER&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11
import sys
sys.stdin = open('input.txt', 'r')

def dfs(arr):
    global answer
    if len(arr) == M and sum([x[1] for x in arr]) == K:
        answer += 1
    for i, x in enumerate(lst):
        if not arr or arr[-1][0] < i:
            dfs(arr+[(i,x)])

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    answer = 0
    dfs([])
    print(f'#{tc} {answer}')
