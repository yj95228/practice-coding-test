# 1차 제출: (풀이시간 90분) 달팽이 방향이 너무 헷갈림
# 2차 제출: 달팽이 처음 위치 visit 처리 안함
# 3차 제출: 격자를 벗어나는 경우 방향 전환해서 술래 없으면 움직이지 않는다는 조건 처리 실수 보완
# 4차 제출: 달팽이 진행방향대로 가고 전환 가능할 때만 바꿀 수 있도록 코드 변경
# 5차 제출: 코드트리에서 테스트케이스 제공해주는 줄 몰랐음 (113ms, 31MB, 4시간 정도 걸린듯)
# - 술래가 움직일 수 없으면 new_matrix에 복사를 안 했음
# - 술래랑 거리가 멀면 이미 도망친 도망자를 추가하지 않고 덮어쓰는 실수함

# https://www.codetree.ai/training-field/frequent-problems/problems/hide-and-seek/description?page=3&pageSize=20
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M, H, K = map(int, input().split())
dt = ((0,1),(1,0),(-1,0),(0,-1))
matrix = [[None]*N for _ in range(N)]       # 도망자
snail = [[False]*N for _ in range(N)]       # 달팽이 그릴 공간
snail_dt = ((-1,0),(0,1),(1,0),(0,-1))      # 달팽이 시계 방향
r_snail_dt = ((1,0),(0,1),(-1,0),(0,-1))    # 달팽이 반시계 방향
sr, sc, sd = N//2, N//2, 0                  # 술래 위치, 방향
snail[sr][sc] = True
clock = True                                # 달팽이 방향
tree = [[False]*N for _ in range(N)]        # 나무 위치
answer = 0
for _ in range(M):
    x, y, d = map(lambda x: int(x)-1, input().split())
    matrix[x][y] = [d]
for _ in range(H):
    x, y = map(int, input().split())
    tree[x-1][y-1] = True

# K턴 동안
for turn in range(1,K+1):
    # 도망자 움직이기
    new_matrix = [[None]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not matrix[r][c]: continue
            elif abs(r-sr)+abs(c-sc) > 3:
                new_matrix[r][c] = [*new_matrix[r][c], *matrix[r][c]] if new_matrix[r][c] else matrix[r][c]
                continue
            for d in matrix[r][c]:
                dx, dy = dt[d]
                # 격자를 벗어나는 경우 방향 반대로 움직여서 술래가 없으면 1칸 이동
                if not (0 <= r+dx < N and 0 <= c+dy < N):
                    dx, dy = -dx, -dy
                    d = 3-d
                # 술래가 없으면 움직인다 (있으면 움직이지 않는다)
                nx, ny = r+dx, c+dy
                if (nx,ny) == (sr,sc):
                    new_matrix[r][c] = [*new_matrix[r][c], d] if new_matrix[r][c] else [d]
                else:
                    new_matrix[nx][ny] = [*new_matrix[nx][ny], d] if new_matrix[nx][ny] else [d]

    # (sr,sc): 술래 현재 위치 / (dx,dy): 술래 움직일 방향 / (nx,ny): 술래 움직인 다음 위치
    dx, dy = snail_dt[sd] if clock else r_snail_dt[sd]
    nx, ny = sr+dx, sc+dy
    snail[nx][ny] = True
    sr, sc = nx, ny

    # 달팽이 다 돌았으면 뱡향 바꾸기
    if (sr, sc) == (0,0):
        clock = False
        snail = [[False]*N for _ in range(N)]
        snail[sr][sc] = True
        sd = 0
    elif (sr, sc) == (N//2,N//2):
        clock = True
        snail = [[False]*N for _ in range(N)]
        snail[sr][sc] = True
        sd = 0
    else:
        # 이동방향이 틀어지는 지점이라면 방향 바꿔주기
        if clock:
            dx, dy = snail_dt[(sd+1)%4]
            nx, ny = sr+dx, sc+dy
            if not snail[nx][ny]: sd = (sd+1)%4
        else:
            dx, dy = r_snail_dt[sd]
            nx, ny = sr+dx, sc+dy
            if not (0 <= nx < N and 0 <= ny < N) or snail[nx][ny]: sd = (sd+1)%4
        dx, dy = snail_dt[sd] if clock else r_snail_dt[sd]

    # 술래잡기
    score = 0
    for i in range(3):
        nr, nc = sr+i*dx, sc+i*dy
        if not (0 <= nr < N and 0 <= nc < N): break
        elif tree[nr][nc]: continue
        elif new_matrix[nr][nc]:
            score += len(new_matrix[nr][nc])
            new_matrix[nr][nc] = None
    answer += turn*score
    matrix = new_matrix

print(answer)