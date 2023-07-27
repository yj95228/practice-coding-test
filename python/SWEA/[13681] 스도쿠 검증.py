# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7wsBZKSv0DFARO&probBoxId=AYmUe0968nYDFARi&type=USER&problemBoxTitle=04_230727&problemBoxCnt=4
import sys
sys.stdin = open("input.txt", "rt")

def garo(matrix):
    for i in range(len(matrix)):
        if len(set(matrix[i])) != 9:
            return False
    return True

def sero(matrix):
    for i in range(len(matrix)):
        if len(set(row[i] for row in matrix)) != 9:
            return False
    return True

def small9(matrix):
    for i in range(0,9,3):
        for j in range(0,9,3):
            arr = list(row[j:j+3] for row in matrix[i:i+3])
            if len(set([x for row in arr for x in row])) != 9:
                return False
    return True

T = int(input())
for tc in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {1 if garo(matrix) and sero(matrix) and small9(matrix) else 0}')