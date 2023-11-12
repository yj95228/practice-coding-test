import sys
input = sys.stdin.readline

def solve():
    turn = 0
    queue = [(sr, sc)]
    while queue:
        next_q = []
        for r, c in queue:
            if (r, c) == (er, ec):
                return turn
            for d, (dx, dy) in enumerate(dt):
                for ddx, ddy in dd[d]:
                    nnx, nny = r+ddx, c+ddy
                    if (nnx, nny) == (er, ec): break
                else:
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < 10 and 0 <= ny < 9 and not V[nx][ny]:
                        V[nx][ny] = 1
                        next_q.append((nx, ny))
        queue = next_q
        turn += 1
    return -1

sr, sc = map(int, input().split())
er, ec = map(int, input().split())
dt = ((3,2),(2,3),(-2,3),(-3,2),(-3,-2),(-2,-3),(2,-3),(3,-2))
dd = (((1,0),(2,1)),((0,1),(1,2)),((0,1),(-1,2)),((-1,0),(-2,1)),((-1,0),(-2,-1)),((0,-1),(-1,-2)),((0,-1),(1,-2)),((1,0),(2,-1)))
V = [[0]*9 for _ in range(10)]
V[sr][sc] = 1
print(solve())