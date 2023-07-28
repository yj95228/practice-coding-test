# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYmXiHj6xx8DFAUe&probBoxId=AYmbEeqKCscDFARi&type=USER&problemBoxTitle=05_230728%3A+Test01&problemBoxCnt=3
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mn, mx = 10, 0
    answer = 0
    for r in range(1,N-1):
        for c in range(1,N-1):
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                if arr[r][c] <= arr[r+dx][c+dy]:
                    break
            else:
                answer += 1
                mn = min(mn, arr[r][c])
                mx = max(mx, arr[r][c])
    print(f'#{tc} {-1 if answer <= 1 else mx-mn}')