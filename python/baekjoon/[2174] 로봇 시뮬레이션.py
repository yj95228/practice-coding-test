from sys import stdin
input = stdin.readline

def move(idx, command, K):
    global matrix
    for _ in range(K):
        narr = [row[:] for row in matrix]
        r, c, d = robot[idx]
        if command == 'L':
            nd = (d+1)%4
            robot[idx] = [r, c, nd]
        elif command == 'R':
            nd = (d-1)%4
            robot[idx] = [r, c, nd]
        else:
            dx, dy = dt[d]
            nx, ny = r+dx, c+dy
            if 0 <= nx < B and 0 <= ny < A:
                if not matrix[nx][ny]:
                    robot[idx] = [nx, ny, d]
                    narr[nx][ny], narr[r][c] = narr[r][c], narr[nx][ny]
                    matrix = narr
                else:
                    print(f'Robot {idx} crashes into robot {matrix[nx][ny]}')
                    return True
            else:
                print(f'Robot {idx} crashes into the wall')
                return True

A, B = map(int, input().split())
matrix = [[0]*A for _ in range(B)]
N, M = map(int, input().split())
dt = ((-1,0),(0,-1),(1,0),(0,1))
dts = {'N':0, 'W':1, 'S':2, 'E':3}
robot = [[]]
for idx in range(1, N+1):
    x, y, d = input().split()
    robot.append([B-(int(y)), int(x)-1, dts[d]])
    matrix[B-(int(y))][int(x)-1] = idx
for _ in range(M):
    idx, command, K = input().split()
    if move(int(idx), command, int(K)):
        break
else:
    print('OK')