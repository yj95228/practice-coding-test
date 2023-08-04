import sys

sys.stdin = open('input.txt','r')

T = int(input())
ROCK, NORMAL, SAFE, MAGMA, HERE = 0, 1, 2, 3, 4
for tc in range(1,T+1):
    def solve():
        N, M = map(int, input().split())
        matrix = []
        queue = []
        R, C = 0, 0
        for r in range(N):
            line = list(map(int, input().split()))
            matrix.append(line)
            if HERE in line:
                R, C = r, line.index(HERE)
            if MAGMA in line:
                for m in range(M):
                    if line[m] == MAGMA: queue.append((MAGMA,r,m))
        queue.append((HERE,R,C))
        distance = [[0]*M for _ in range(N)]
        while queue:
            where, r, c = queue.pop(0)
            if where == HERE and matrix[r][c] == SAFE: return distance[r][c]
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= r+dx < N and 0 <= c+dy < M and not distance[r+dx][c+dy] and\
                ((where == MAGMA and matrix[r+dx][c+dy] == NORMAL)
                or (where == HERE and (matrix[r+dx][c+dy] == NORMAL or matrix[r+dx][c+dy] == SAFE))):
                    distance[r+dx][c+dy] = distance[r][c] + 1
                    queue.append((where, r+dx, c+dy))
    print(f'#{tc} {solve() or -1}')