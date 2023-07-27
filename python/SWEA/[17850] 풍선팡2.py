# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYmCoVyqlLYDFAUe&probBoxId=AYmCPbwako0DFAUe&type=USER&problemBoxTitle=01_230724&problemBoxCnt=6
#import sys
#sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    answer = 0
    for i in range(N):
        for j in range(M):
            tmp = lst[i][j]
            if i > 0:
                tmp += lst[i-1][j]
            if i < N-1:
                tmp += lst[i+1][j]
            if j > 0:
                tmp += lst[i][j - 1]
            if j < M-1:
                tmp += lst[i][j + 1]
            if tmp > answer:
                answer = tmp
    print(f'#{tc} {answer}')

# 두번째 풀이
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(M):
            tmp = 0
            tmp += arr[r][c]
            if r > 0: tmp += arr[r-1][c]
            if r < N-1: tmp += arr[r+1][c]
            if c > 0: tmp += arr[r][c-1]
            if c < M-1: tmp += arr[r][c+1]
            if answer < tmp: answer = tmp
    print(f'#{tc} {answer}')

# 세번째 풀이
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(M):
            sm = 0
            sm += arr[r][c]
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                if 0 <= r+dx < N and 0 <= c+dy < M:
                    sm += arr[r+dx][c+dy]
            answer = max(answer, sm)
    print(f'#{tc} {answer}')

# 네번째 풀이
def check(matrix, r, c):
    result = 0
    for dx, dy in ((0,0),(1,0),(0,1),(-1,0),(0,-1)):
        if 0 <= r+dx < len(matrix) and 0 <= c+dy < len(matrix[0]):
            result += matrix[r+dx][c+dy]
    return result

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(M):
            answer = max(answer, check(matrix, r, c))
    print(f'#{tc} {answer}')