import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def recur(rr, cc, result):
    global answer
    answer = max(answer, result)
    for r in range(N-1):
        for c in range(M-1):
            if r <= rr and c <= cc: continue
            for bumerang in bumerangs:
                visited, sm = [], 0
                for rate, dx, dy in bumerang:
                    nx, ny = r+dx, c+dy
                    if V[nx][ny]: break
                else:
                    for rate, dx, dy in bumerang:
                        nx, ny = r+dx, c+dy
                        V[nx][ny] = 1
                        visited.append((nx, ny))
                        sm += rate*A[nx][ny]
                    recur(r, c, result+sm)
                    for x, y in visited:
                        V[x][y] = 0

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
bumerangs = [
    [(1,0,0),(2,0,1),(1,1,1)],
    [(1,0,1),(1,1,0),(2,1,1)],
    [(1,0,0),(2,1,0),(1,1,1)],
    [(2,0,0),(1,0,1),(1,1,0)]
]
V = [[0]*M for _ in range(N)]
answer = 0
recur(-1, -1, 0)
print(answer)