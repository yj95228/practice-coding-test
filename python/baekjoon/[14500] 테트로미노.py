# 1차 시도 -> 범위 체크 안하려고 0으로 패딩
# 2차 시도 -> 혹시 0으로 패딩했을 때 반례가 있을까봐 범위 체크하여 최댓값 구하기
# 3차 시도 -> 앞의 시도들에서 대칭/회전 빼먹은 케이스 있어서 1차 시도 코드에서 4가지 추가 (성공, 118704kb, 232ms)
# 4차 시도 -> 앞의 코드 너무 노가다라서 코드 짧게 (117116kb, 344ms)
# 5차 시도 -> 패딩을 3칸만 해도 되는데 4칸이나 해서 3차 시도 코드를 수정해서 제출 (118704kb, 228ms)
# 6차 시도 -> 패딩을 3칸만 해도 되는데 4칸이나 해서 4차 시도 코드를 수정해서 제출 (117116kb, 372ms)
# https://www.acmicpc.net/problem/14500
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 노가다했지만 시간은 더 빠른 코드
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) + [0]*3 for _ in range(N)] + [[0]*(M+3) for _ in range(3)]
answer = 0
for r in range(N):
    for c in range(M):
        answer = max(answer, max([
            matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r][c+3],
            matrix[r][c] + matrix[r+1][c] + matrix[r+2][c] + matrix[r+3][c],
            matrix[r][c] + matrix[r+1][c] + matrix[r][c+1] + matrix[r+1][c+1],
            matrix[r][c] + matrix[r+1][c] + matrix[r+2][c] + matrix[r+2][c+1],
            matrix[r][c+1] + matrix[r+1][c+1] + matrix[r+2][c+1] + matrix[r+2][c],
            matrix[r][c] + matrix[r][c+1] + matrix[r+1][c+1] + matrix[r+2][c+1],
            matrix[r][c] + matrix[r][c+1] + matrix[r+1][c] + matrix[r+2][c],
            matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r+1][c],
            matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r+1][c+2],
            matrix[r][c] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2],
            matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2] + matrix[r][c+2],
            matrix[r][c] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+2][c+1],
            matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+2][c],
            matrix[r][c+1] + matrix[r][c+2] + matrix[r+1][c] + matrix[r+1][c+1],
            matrix[r][c] + matrix[r][c+1] + matrix[r+1][c+1] + matrix[r+1][c+2],
            matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+2][c+1],
            matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r+1][c+1],
            matrix[r][c] + matrix[r+1][c] + matrix[r+2][c] + matrix[r+1][c+1],
            matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2]
        ]))
print(answer)

# 간결하지만 시간은 더 오래 걸리는 코드
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) + [0]*3 for _ in range(N)] + [[0]*(M+3) for _ in range(4)]
dt = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(2,0),(2,1),(3,0)]
# 0 1 2 3
# 4 5 6
# 7 8
# 9
tetris = [(0,1,2,3),(0,4,7,9),
          (0,1,4,5),
          (0,4,7,8),(0,1,5,8),(1,5,8,7),(0,1,4,7),(0,1,2,4),(0,1,2,6),(2,4,5,6),(0,4,5,6),
          (0,4,5,8),(1,4,5,7),(1,2,4,5),(0,1,5,6),
          (1,4,5,8),(0,1,2,5),(0,4,7,5),(1,4,5,6)]
answer = 0
for r in range(N):
    for c in range(M):
        for t in tetris:
            sm = 0
            for i in range(4):
                dx, dy = dt[t[i]]
                sm += matrix[r+dx][c+dy]
            answer = max(answer, sm)
print(answer)