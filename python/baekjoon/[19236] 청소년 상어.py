# 1차 제출: 성환님의 도움을 받아 제출 성공 (115316kb, 132ms)
'''
- 2차원 배열 복사가 아닌 3차원 배열 복사를 했어야 함
    - [[x[:] for x in rows] for rows in new_matrix]
- new_matrix[nx][ny] = None -> ~[0], ~[1] = -1, -1 / fish, d와 같이 수정
'''
# 2차 제출: new_matrix2로 만들지 않고 new_matrix 한번만 만들어도 됨
# -1보다는 None이 더 pythonic한 방식이라고 생각되어서 코드 변경
# https://www.acmicpc.net/problem/19236
import sys
input = sys.stdin.readline

def recur(matrix, sr, sc, sd, result):
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
        if not (0 <= nx < 4 and 0 <= ny < 4): break
        elif not new_matrix[nx][ny][0]: continue

        fish, d = new_matrix[nx][ny]
        dead[fish] = True
        new_matrix[nx][ny] = [None, None]

        recur(new_matrix, nx, ny, d, result+fish+1)

        dead[fish] = False
        new_matrix[nx][ny] = [fish, d]


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
    matrix[0][0] = [None, None]

# 물고기와 상어 이동
recur(matrix, 0, 0, sd, answer)
print(answer)