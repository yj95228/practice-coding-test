# https://www.acmicpc.net/problem/19236
import sys
input = sys.stdin.readline

def recur(matrix, sr,sc,sd,result):
    global answer
    answer = max(result, answer)

    new_matrix = [[x[:] for x in rows] for rows in matrix]

    # 물고기 이동
    for fish in range(16):
        if not dead[fish]:
            new_matrix = fish_move(new_matrix, fish, sr, sc)

    # 상어 이동
    dx, dy = dt[sd]
    for i in range(1,4):
        nx, ny = sr+i*dx, sc+i*dy
        new_matrix2 = [[x[:] for x in rows] for rows in new_matrix]
        if not (0 <= nx < 4 and 0 <= ny < 4): break
        elif new_matrix2[nx][ny][0] == -1: continue

        fish, d = new_matrix2[nx][ny]
        dead[fish] = True
        new_matrix2[nx][ny][0], new_matrix2[nx][ny][1] = -1,-1
        result += fish+1

        recur(new_matrix2, nx,ny,d,result)

        result -= fish+1
        dead[fish] = False
        new_matrix2[nx][ny][0], new_matrix2[nx][ny][1] = fish, d


def fish_move(matrix, fish, sr, sc):
    for r in range(4):
        for c in range(4):
            if matrix[r][c] and matrix[r][c][0] == fish:
                d = matrix[r][c][1]
                dx, dy = dt[d]
                nx, ny = r+dx, c+dy
                turn = 0

                # 범위 밖이거나 상어 있으면
                while True:
                    if turn == 8: break
                    elif (0 <= nx < 4 and 0 <= ny < 4) and (nx,ny) != (sr,sc):
                        matrix[r][c], matrix[nx][ny] = matrix[nx][ny], matrix[r][c]
                        matrix[nx][ny][1] = d
                        return matrix

                    turn += 1
                    d = (d+1)%8
                    dx, dy = dt[d]
                    nx, ny = r+dx, c+dy
    return matrix

matrix = [[[] for _ in range(4)] for _ in range(4)]
#  ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dt = ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1))
for r in range(4):
    ipt = list(map(lambda x: int(x)-1, input().split()))
    for c in range(4):
        matrix[r][c] = [ipt[2*c], ipt[2*c+1]]

sr, sc, sd, answer = 0, 0, 0, 0
dead = [False]*16
if matrix[0][0]:
    fish, sd = matrix[0][0]
    dead[fish] = True
    sr, sc = 0, 0
    answer += fish+1
    matrix[0][0] = [-1,-1]

# 물고기와 상어 이동
recur(matrix, 0, 0, sd, answer)
print(answer)