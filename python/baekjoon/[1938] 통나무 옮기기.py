from sys import stdin
from collections import deque
input = stdin.readline

def solve():
    turn = 0
    while queue:
        for _ in range(len(queue)):
            namu = queue.popleft()
            for r, c in namu:
                if (r, c) not in end:
                    break
            else: return turn

            # U, D, L, R
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                namus = []
                for r, c in namu:
                    nx, ny = r+dx, c+dy
                    if A[nx][ny]: break
                    namus.append((nx, ny))
                else:
                    v = ''.join(map(str, namus))
                    if v in visited: continue
                    visited.add(v)
                    queue.append(namus)

            # T
            minr, minc, maxr, maxc = N, N, 0, 0
            for r, c in namu:
                minr = min(minr, r)
                minc = min(minc, c)
                maxr = max(maxr, r)
                maxc = max(maxc, c)
            flag = False
            if maxr == minr:
                minr -= 1
                maxr += 1
                for r in range(minr, maxr+1):
                    for c in range(minc, maxc+1):
                        if A[r][c]:
                            flag = True
                            break
                    if flag: break
                if not flag:
                    mid = (minc+maxc)//2
                    namus = [(minr, mid), (minr+1, mid), (maxr, mid)]
                    v = ''.join(map(str, namus))
                    if v in visited: continue
                    visited.add(v)
                    queue.append(namus)
            else:
                minc -= 1
                maxc += 1
                for r in range(minr, maxr+1):
                    for c in range(minc, maxc+1):
                        if A[r][c]:
                            flag = True
                            break
                    if flag: break
                if not flag:
                    mid = (minr+maxr)//2
                    namus = [(mid, minc), (mid, minc+1), (mid, maxc)]
                    v = ''.join(map(str, namus))
                    if v in visited: continue
                    visited.add(v)
                    queue.append(namus)
        turn += 1
    return 0

N = int(input())
A = [[1]*(N+2)] + [[1] + list(input().rstrip()) + [1] for _ in range(N)] + [[1]*(N+2)]
start, end = [], []
for r in range(1, N+1):
    for c in range(1, N+1):
        if A[r][c] == 'B':
            start.append((r, c))
            A[r][c] = 0
        elif A[r][c] == 'E':
            end.append((r, c))
            A[r][c] = 0
        else:
            A[r][c] = int(A[r][c])
queue = deque([start])
visited = set()
visited.add(''.join(map(str,start)))
print(solve())

# 2차 풀이 (204ms -> 180ms)
def solve():
    sr, sc = start[1]
    dd = 0

    if start[0][0] == sr:
        V[GARO][sr][sc] = 1
    else:
        V[SERO][sr][sc] = 1
        dd = 1

    queue = deque([(dd, sr, sc)])
    turn = 0
    while queue:
        for _ in range(len(queue)):
            dd, r, c = queue.popleft()
            tree = [(r, c)]
            if dd == GARO:
                tree.extend([(r, c - 1), (r, c + 1)])
            else:
                tree.extend([(r - 1, c), (r + 1, c)])

            # 도착 여부
            three = True
            for rr, cc in tree:
                if (rr, cc) in end:
                    three &= 1
                else: three = 0
            if three: return turn

            # UDLR
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = r + dx, c + dy
                if V[dd][nx][ny]: continue
                for rr, cc in tree:
                    nnx, nny = rr + dx, cc + dy
                    if A[nnx][nny]: break
                else:
                    V[dd][nx][ny] = 1
                    queue.append((dd, nx, ny))

            # 회전
            dd ^= 1
            flag = False
            if V[dd][r][c]: continue
            for dx in [-1,0,1]:
                if flag: break
                for dy in [-1,0,1]:
                    if A[r + dx][c + dy]:
                        flag = True
                        break
            if not flag:
                V[dd][r][c] = 1
                queue.append((dd, r, c))
        turn += 1
    return 0

N = int(input())
A = [[1]*(N+2)] + [[1] + list(input().rstrip()) + [1] for _ in range(N)] + [[1]*(N+2)]
V = [[[0]*(N+2) for _ in range(N+2)] for _ in range(2)] # 중간지점 기준 가로/세로
start, end = [], []
GARO, SERO = 0, 1
for r in range(1, N+1):
    for c in range(1, N+1):
        if A[r][c] == 'B':
            A[r][c] = 0
            start.append((r, c))
        elif A[r][c] == 'E':
            A[r][c] = 0
            end.append((r, c))
        else:
            A[r][c] = int(A[r][c])

print(solve())