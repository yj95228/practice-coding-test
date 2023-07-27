# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7wyBz6S1cDFARO&probBoxId=AYmUe0968nYDFARi&type=USER&problemBoxTitle=04_230727&problemBoxCnt=4
import sys
sys.stdin = open("input.txt", "rt")

def canGo(matrix, r, c, d):
    if 0 <= r - 1 < len(matrix) and matrix[r - 1][c] == 1:
        r -= 1
        return r, c, 0
    return r, c, d

for _ in range(10):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    r, c, d = len(matrix)-1, matrix[99].index(2), 0
    while r > 0:
        # 오른쪽으로 가는 중이 아니었고 왼쪽으로 갈 수 있으면
        if d != 1 and 0 <= c-1 < len(matrix[0]) and matrix[r][c-1] == 1:
            c -= 1
            d = -1
            # 근데 위로 갈 수 있으면 가기
            r, c, d = canGo(matrix, r, c, d)
        # 왼쪽으로 가는 중이 아니었고 오른쪽으로 갈 수 있으면
        elif d != -1 and 0 <= c+1 < len(matrix[0]) and matrix[r][c+1] == 1:
            c += 1
            d = 1
            # 근데 위로 갈 수 있으면 가기
            r, c, d = canGo(matrix, r, c, d)
        # 둘다 못가면 위로
        else:
            r, c, d = canGo(matrix, r, c, d)
    print(f'#{T} {c}')

# 강사님 코드
T = 10
for tc in range(1, T+1):
    _ = input()
    arr = [['0']+list(input().split())+['0'] for _ in range(100)]
    ci, cj = 99, 1
    while cj <= 100:
        if arr[ci][cj] == '2':
            break
        cj += 1

    while ci > 0:
        arr[ci][cj] = '0'
        if arr[ci][cj-1] == '1':
            cj -= 1
        elif arr[ci][cj+1] == '1':
            cj += 1
        else:
            ci -= 1
    print(f'#{tc} {cj-1}')