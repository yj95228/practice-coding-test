def white(idx, r, c, d):
    floor = G[r][c].index(idx)
    dx, dy = dt[d]
    nx, ny = r + dx, c + dy
    for i in range(floor, len(G[r][c])):
        horse = G[r][c][i]
        horses[horse][0], horses[horse][1] = nx, ny
    G[nx][ny].extend(G[r][c][floor:])
    G[r][c] = G[r][c][:floor]
    return len(G[nx][ny]) >= 4

def red(idx, r, c, d):
    floor = G[r][c].index(idx)
    dx, dy = dt[d]
    nx, ny = r + dx, c + dy
    for i in range(floor, len(G[r][c])):
        horse = G[r][c][i]
        horses[horse][0], horses[horse][1] = nx, ny
    G[nx][ny].extend(G[r][c][floor:][::-1])
    G[r][c] = G[r][c][:floor]
    return len(G[nx][ny]) >= 4

def blue(idx, r, c, d):
    floor = G[r][c].index(idx)
    dx, dy = dt[d ^ 1]
    nx, ny = r + dx, c + dy
    result = False
    if A[nx][ny] == 0:
        result = white(idx, r, c, d^1)
    elif A[nx][ny] == 1:
        result = red(idx, r, c, d^1)
    horses[idx][-1] ^= 1
    return result

N, K = map(int, input().split())
A = [[2] * (N + 2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + [[2] * (N + 2)]
dt = ((0, 1), (0, -1), (-1, 0), (1, 0))
horses = []
G = [[[] for _ in range(N + 2)] for _ in range(N + 2)]
for idx in range(K):
    x, y, d = map(int, input().split())
    horses.append([x, y, d - 1])
    G[x][y].append(idx)

flag = False
for turn in range(1, 1001):
    for idx in range(K):

        flag = False
        r, c, d = horses[idx]
        dx, dy = dt[d]
        nx, ny = r + dx, c + dy

        if A[nx][ny] == 0:
            if white(idx, r, c, d):
                flag = True
                break
        elif A[nx][ny] == 1:
            if red(idx, r, c, d):
                flag = True
                break
        else:
            if blue(idx, r, c, d):
                flag = True
                break

    if flag:
        print(turn)
        break

else: print(-1)