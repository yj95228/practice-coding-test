'''
- 최대값 갱신해주는거랑 냄새 줄이는거 자꾸 까먹음
- 1차. TC 2번 죽은 애들 안 없애줌
- 2차. TC 4번 몬스터가 안 죽은 곳에도 냄새를 뿌려줌 + 이동할 때 여러 마리 이동시켜야 되는데 한 마리로만 이동시킴
- 3차. TC 31번 아무 곳도 갈 데가 없다면 상상상으로 가야하는데 똑같은 실수함...
'''
# https://www.codetree.ai/training-field/frequent-problems/problems/pacman?page=1&pageSize=20
from sys import stdin
input = stdin.readline

matrix = [[[0]*8 for _ in range(4)] for _ in range(4)]
dt = ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1))    # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
M, T = map(int, input().split())                   # 몬스터의 마리 수 m과 진행되는 턴의 수 t
sr, sc = map(lambda x: int(x)-1, input().split())  # 팩맨의 격자에서의 초기 위치
monsters = []
for _ in range(M):
    r, c, d = map(lambda x: int(x)-1, input().split())
    matrix[r][c][d] += 1

smell = [[0]*4 for _ in range(4)]
for _ in range(T):
    # 1. 몬스터 복제 시도
    copies = [[x[:] for x in row] for row in matrix]

    # 2. 몬스터 이동
    narr = [[[0]*8 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for d in range(8):
                if not matrix[r][c][d]: continue
                for i in range(8):
                    nd = (d+i)%8
                    dx, dy = dt[nd]
                    nx, ny = r+dx, c+dy
                    # 갈 수 있다면
                    if 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny] and (nx,ny) != (sr,sc):
                        narr[nx][ny][nd] += matrix[r][c][d]
                        break
                else:
                    narr[r][c][d] += matrix[r][c][d]

    # 3. 팩맨 이동
    where = []
    nsr, nsc, mx = None, None, -1
    for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
        nx, ny = sr+dx, sc+dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
                nnx, nny = nx+dx, ny+dy
                if 0 <= nnx < 4 and 0 <= nny < 4:
                    for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
                        nnnx, nnny = nnx+dx, nny+dy
                        if 0 <= nnnx < 4 and 0 <= nnny < 4:
                            s = set()
                            s.add((nx,ny))
                            s.add((nnx,nny))
                            s.add((nnnx,nnny))
                            result = 0
                            for r, c in s:
                                result += sum(narr[r][c])
                            if result > mx:
                                mx = result
                                where = [row[:] for row in s]
                                nsr, nsc = nnnx, nnny

    sr, sc = nsr, nsc
    # 4. 죽은 물고기 없애주기 + 몬스터 냄새
    for r, c in where:
        if any(narr[r][c]):
            smell[r][c] = 3
            narr[r][c] = [0]*8

    # 5. 몬스터 시체 소멸 + 몬스터 복제 완성
    for r in range(4):
        for c in range(4):
            smell[r][c] = max(0, smell[r][c]-1)
            for d in range(8):
                matrix[r][c][d] = narr[r][c][d] + copies[r][c][d]

print(sum([fish for row in matrix for fishes in row for fish in fishes]))