# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnIy86qE3wDFAUe&probBoxId=AYnNE126270DFARi&type=USER&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11
import sys

def solve(x):
    if x == 1:
        print(x)
        return ''
    else:
        print(x, end=' ')
        return solve(x-1)
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}', end=' ')
    print(solve(N), end='')