# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX81KpYq2yQDFAQe&probBoxId=AYpJUI9690oDFAQI+&type=USER&problemBoxTitle=28_230831%3A+%EC%8B%A4%EC%A0%84%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=4
import sys
sys.stdin = open('input.txt', 'r')

def dfs(r,c,turn):
    global x,y,answer
    if turn == 0:
        if 0 <= r+1 < N and 0 <= c+1 < N and not visited[r+1][c+1]\
        and matrix[r+1][c+1] not in dessert:
            dessert.add(matrix[r+1][c+1])
            visited[r+1][c+1] = True
            dfs(r+1,c+1,0)
            dessert.remove(matrix[r+1][c+1])
            visited[r+1][c+1] = False
        if 0 <= r+1 < N and 0 <= c-1 < N and not visited[r+1][c-1]\
        and matrix[r+1][c-1] not in dessert:
            dessert.add(matrix[r+1][c-1])
            visited[r+1][c-1] = True
            dfs(r+1,c-1,1)
            dessert.remove(matrix[r+1][c-1])
            visited[r+1][c-1] = False
    elif turn == 1:
        if 0 <= r+1 < N and 0 <= c-1 < N and not visited[r+1][c-1]\
        and matrix[r+1][c-1] not in dessert:
            dessert.add(matrix[r+1][c-1])
            visited[r+1][c-1] = True
            dfs(r+1,c-1,1)
            dessert.remove(matrix[r+1][c-1])
            visited[r+1][c-1] = False
        if 0 <= r-1 < N and 0 <= c-1 < N and not visited[r-1][c-1]\
        and matrix[r-1][c-1] not in dessert:
            dessert.add(matrix[r-1][c-1])
            visited[r-1][c-1] = True
            dfs(r-1,c-1,2)
            dessert.remove(matrix[r-1][c-1])
            visited[r-1][c-1] = False
    elif turn == 2:
        if 0 <= r-1 < N and 0 <= c-1 < N and not visited[r-1][c-1]\
        and matrix[r-1][c-1] not in dessert:
            dessert.add(matrix[r-1][c-1])
            visited[r-1][c-1] = True
            dfs(r-1,c-1,2)
            dessert.remove(matrix[r-1][c-1])
            visited[r-1][c-1] = False
        if 0 <= r-1 < N and 0 <= c+1 < N and not visited[r-1][c+1]\
        and matrix[r-1][c+1] not in dessert:
            dessert.add(matrix[r-1][c+1])
            visited[r-1][c+1] = True
            dfs(r-1,c+1,3)
            dessert.remove(matrix[r-1][c+1])
            visited[r-1][c+1] = False
    else:
        if (r,c) == (x,y):
            answer = max(answer, len(dessert))
            return
        elif 0 <= r-1 < N and 0 <= c+1 < N and not visited[r-1][c+1]\
        and matrix[r-1][c+1] not in dessert:
            dessert.add(matrix[r-1][c+1])
            visited[r-1][c+1] = True
            dfs(r-1,c+1,3)
            dessert.remove(matrix[r-1][c+1])
            visited[r-1][c+1] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    for r in range(N):
        for c in range(N):
            visited = [[False]*N for _ in range(N)]
            x, y = r, c
            dessert = set()
            dfs(r,c,0)
    print(f'#{tc} {answer}')