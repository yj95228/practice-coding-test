# 한 달 전의 나(7/26): 뒤쪽 칸을 후진할 수 있는지만 체크하고 벽인지 체크하지 않아서 2차 제출만에 성공 (114488kb, 136ms)
# 3차 제출: (25분 소요) 113112kb, 116ms
# 과거 코드와의 차이
# - 주변 4칸을 청소할 수 있는지 함수로 빼지 않고 그냥 써내려감
# - 벽을 미리 만들어서 범위 체크를 하지 않아도 되게 만듬
# - 탐색만 하면 되므로 input 받을때 string 그대로 받음
# https://www.acmicpc.net/problem/14503
import sys

def check4direction(matrix, r, c):
    for i in range(4):
        if 0 <= r+dx[i] < N and 0 <= c+dy[i] < M and matrix[r+dx[i]][c+dy[i]] == 0:
            return False # 청소 안 되어 있음
    return True

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
answer = 0
matrix = [list(map(int, input().split())) for _ in range(N)]
while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if matrix[r][c] == 0:
        answer += 1
        matrix[r][c] = 2
    else:
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        if not check4direction(matrix, r, c):
            # 반시계 방향으로 90도 회전한다.
            d = 3 if d == 0 else d-1
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if 0 <= r+dx[d] < N and 0 <= c+dy[d] < M and matrix[r+dx[d]][c+dy[d]] == 0:
                r, c = r+dx[d], c+dy[d]
                # 1번으로 돌아간다.
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        else:
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if 0 <= r-dx[d] < N and 0 <= c-dy[d] < M and matrix[r-dx[d]][c-dy[d]] != 1:
                r, c = r-dx[d], c-dy[d]
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            elif not (0 <= r-dx[d] < N and 0 <= c-dy[d] < M)\
            or (0 <= r-dx[d] < N and 0 <= c-dy[d] < M and matrix[r-dx[d]][c-dy[d]] == 1):
                print(answer)
                break

# 두번째 풀이
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
DIRTY, WALL, CLEAN = '0', '1', '2'
dt = ((-1,0),(0,1),(1,0),(0,-1))    # ^ > v <
matrix = [[WALL]*(M+2)] + [[WALL] + list(input().split()) + [WALL] for _ in range(N)] + [[WALL]*(M+2)]
answer = 0
r, c = r+1, c+1
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if matrix[r][c] == DIRTY:
        matrix[r][c] = CLEAN
        answer += 1

    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    for dx, dy in dt:
        if matrix[r+dx][c+dy] == DIRTY:
            # 반시계 방향으로 90도 회전한다.
            d = (d-1)%4
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            dx, dy = dt[d]
            if matrix[r+dx][c+dy] == DIRTY:
                r, c = r+dx, c+dy
            # 1번으로 돌아간다.
            break

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    else:
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        dx, dy = dt[d]
        if matrix[r-dx][c-dy] != WALL:
            r, c = r-dx, c-dy
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else: break

print(answer)