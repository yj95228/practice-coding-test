# https://www.acmicpc.net/problem/17780
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def move(r, c, nx, ny):
    if matrix[nx][ny] == 0:
        for m in chess[r][c]:
            horse[m] = [nx, ny, horse[m][-1]]
        chess[nx][ny].extend(chess[r][c])
        chess[r][c] = []
    elif matrix[nx][ny] == 1:
        for m in chess[r][c]:
            horse[m] = [nx, ny, horse[m][-1]]
        chess[nx][ny].extend(chess[r][c][1:][::-1] + [k])
        chess[r][c] = []
    
    if len(chess[nx][ny]) >= 4: return True

def blue(k, d):
    d ^= 1
    horse[k][2] = d
    dx, dy = dt[d]
    nx, ny = r+dx, c+dy
    if 0 <= nx < N and 0 <= ny < N:
        return move(r, c, nx, ny)

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]
dt = ((0,1),(0,-1),(-1,0),(1,0))
horse = []
for k in range(K):
    x, y, d = map(lambda x: int(x)-1, input().split())
    horse.append([x, y, d])
    chess[x][y].append(k)

end = False
for turn in range(1,1001):
    for k in range(K):
        r, c, d = horse[k]
        if chess[r][c][0] != k: continue
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] == 2:
                if blue(k, d):
                    end = True
                    break
            else:
                if move(r, c, nx, ny):
                    end = True
                    break
        else:
            if blue(k, d):
                end = True
                break
    if end:
        print(turn)
        break
else: print(-1)