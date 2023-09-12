# 1차 제출 : (소요시간 90분) 배열 돌리기 너무 오래 걸림
# 2차 제출 : (소요시간 105분) 배열 돌리기 인덱스 실수 수정 (186460kb, 2936ms)
# 3차 제출 : 배열을 따로 만들지 않고 바로 대입하기 (2936ms -> 2752ms)
# https://www.acmicpc.net/problem/17144
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 파악
cleaner = []
for r in range(R):
    for c in range(C):
        if matrix[r][c] == -1:
            cleaner.append(r)
            if len(cleaner) == 2: break

for _ in range(T):
    # 미세먼지 확산
    dirty, clean = {}, {}
    for r in range(R):
        for c in range(C):
            # 미세먼지, 확산되는 먼지
            total, result = matrix[r][c], 0
            if matrix[r][c] > 0:
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] >= 0:
                        dirty[(nx,ny)] = dirty[(nx,ny)]+total//5 if (nx,ny) in dirty else total//5
                        result += total//5
                clean[(r,c)] = matrix[r][c] - result

    for r,c in clean:
        matrix[r][c] = clean[(r,c)]
    for r,c in dirty:
        matrix[r][c] += dirty[(r,c)]

    # 공기청정기 작동
    for r in range(cleaner[0],0,-1):
        matrix[r][0] = matrix[r-1][0]
    matrix[0] = matrix[0][1:] + [matrix[1][-1]]
    for r in range(1,cleaner[0]):
        matrix[r][-1] = matrix[r+1][-1]
    matrix[cleaner[0]] = [-1,0] + matrix[cleaner[0]][1:-1]

    for r in range(cleaner[1]+1,R-1):
        matrix[r][0] = matrix[r+1][0]
    matrix[-1] = matrix[-1][1:] + [matrix[-1][-2]]
    for r in range(R-1,cleaner[1],-1):
        matrix[r][-1] = matrix[r-1][-1]
    matrix[cleaner[1]] = [-1,0] + matrix[cleaner[1]][1:-1]

answer = 0
for r in range(R):
    for c in range(C):
        if matrix[r][c] > 0:
            answer += matrix[r][c]
print(answer)