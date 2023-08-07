# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnIy86qE3wDFAUe&probBoxId=AYnNE126270DFARi&type=USER&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11
import sys

# solve(N)로 풀이
def solve(x):
    return 1 if x == 1 or x == 2 else solve(x-1)+solve(x-2)
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [1,1]
    print(f'#{tc} {solve(N)}')

# solve(1)로 풀이
def solve(x):
    if x == N: return arr[x]
    arr[x] = arr[x-1] + arr[x-2]
    return solve(x+1)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [1,1]
    print(f'#{tc} {solve(1)}')