# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYmCpxb6lOEDFAUe&probBoxId=AYmUe0968nYDFARi+&type=USER&problemBoxTitle=04_230727&problemBoxCnt=++4+
import sys
sys.stdin = open("input.txt", "rt")

def check(matrix, r, c, N, M):
    # if N != len(matrix):
    #     print("NO1")
    # if M != len(matrix[0]):
    #     print("NO2")
    result = matrix[r][c]
    for mul in range(1, matrix[r][c]+1): # result를 넣으면 값이 계속 변하니까 matrix[r][c]와 같이 변하지 않는 값으로
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r + dx * mul, c + dy * mul
            if 0 <= nx < N and 0 <= ny < M:
                result += matrix[nx][ny]
    return result

T = int(input())
for tc in range(1, T + 1):
    global N, M
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(M):
            answer = max(answer, check(matrix, r, c, N, M))
    print(f'#{tc} {answer}')