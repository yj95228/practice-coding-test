# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7wsBZKSv0DFARO&probBoxId=AYmUe0968nYDFARi&type=USER&problemBoxTitle=04_230727&problemBoxCnt=4
import sys
sys.stdin = open("input.txt", "rt")

def check(matrix, r, c):
    N = len(matrix)
    if 0 <= r < N and 0 <= c < N and matrix[r][c] == 1:
        return True
    return False

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                for dx, dy in ((0,1),(1,0)):
                    for i in range(-1,K+1):
                        if 0 <= i < K and check(matrix, r+dx*i, c+dy*i) is False:
                            break
                        elif i == -1 and check(matrix, r+dx*i, c+dy*i) is True:
                            break
                        elif i == K and check(matrix, r+dx*i, c+dy*i) is False:
                            answer += 1
    print(f'#{tc} {answer}')

# 강사님 코드
def count(matrix):
    result = 0
    for row in matrix:
        cnt = 0
        for x in row:
            if x == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
    return result

for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    arr_t = list(zip(*arr))     # 전치행렬 만들기 : 튜플형태 (수정할 수 없음)
    arr_t = list(map(list, zip(*arr)))  # 리스트 형태로 전치행렬 만들기
    answer = count(arr) + count(arr_t)
    print(f'#{tc} {answer}')