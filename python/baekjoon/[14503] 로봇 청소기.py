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