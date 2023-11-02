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

# 2차 풀이
def dfs(r, c, d, where, num):
    global answer
    for dd in [0, 1]:
        if d == -1 and dd == 0: continue
        elif d == 3 and dd == 1: continue
        d = (d+dd)%4
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N:
            if V[nx][ny]:
                if (nx, ny) == where[0]:
                    answer = max(answer, len(where))
                    return
            else:
                if A[nx][ny] in num: continue
                V[nx][ny] = 1
                dfs(nx, ny, d, where+[(nx, ny)], num+[A[nx][ny]])
                V[nx][ny] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    V = [[0]*N for _ in range(N)]
    dt = ((1,-1),(1,1),(-1,1),(-1,-1))

    answer = -1
    for r in range(N-2):
        for c in range(1, N-1):
            V[r][c] = 1
            dfs(r, c, -1, [(r,c)], [A[r][c]])
            V[r][c] = 0
    print(f'#{tc} {answer}')

# 3차 풀이
def dfs(r, c, d, num):
    global answer
    dx, dy = dt[d]
    nx, ny = r+dx, c+dy
    if d == 3 and (nx, ny) == (sr, sc):
        answer = max(answer, len(num))
        return
    elif 0 <= nx < N and 0 <= ny < N and A[nx][ny] not in num:
        dfs(nx, ny, d, num+[A[nx][ny]])
        if d != 3:
            dfs(nx, ny, (d+1)%4, num+[A[nx][ny]])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    V = [[0]*N for _ in range(N)]
    dt = ((1,-1),(1,1),(-1,1),(-1,-1))

    answer = -1
    for sr in range(N-2):
        for sc in range(1, N-1):
            dfs(sr, sc, 0, [A[sr][sc]])
    print(f'#{tc} {answer}')
