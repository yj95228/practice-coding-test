# https://www.codetree.ai/training-field/frequent-problems/problems/battle-ground/description?page=1&pageSize=20
'''
- 산타의 선물공장은 N이 커서 싸움땅 올인
- 5분 읽고 자료구조 정해서 풀기 시작
    -> 정해도 짜면서 계속 바뀌네...
    -> 미리 생각하는 힘이 부족한거 같음
- 14:56 일단 제출 (109ms, 31MB)
- 총을 격자에 여러 개 둘 수 있게 리스트로 했어야했는데 처음에 그냥 int로 시작함
- 이긴 사람과 진 사람이 동시에 움직이는 데 해당 처리가 어려웠음
- 가장 센 총을 가져와야 하므로 heapq를 쓰는 것이 바람직함 (sort는 O(nlogn), max, remove는 모두 O(n)임)
- 진 사람이 총을 떨어뜨린 후 이긴 사람이 총을 주워야함
- 방향 탐색할때 while문 말고 for문으로 4방향 탐색하기
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = [list(map(lambda x: [int(x)], input().split())) for _ in range(N)]
where = [[0]*N for _ in range(N)]
dt = ((-1,0),(0,1),(1,0),(0,-1))
players, score = [], [0]*M
for idx in range(1,M+1):
    X, Y, D, S = map(int, input().split())
    players.append([X-1,Y-1,D,S,0])             # (x,y) 위치, d 방향, s 초기 능력치, g: 총
    where[X-1][Y-1] = idx

# 1. 플레이어 순차적으로 본인이 향하던 방향대로 한 칸 이동
for _ in range(K):
    for i in range(M):
        x, y, d, s, g = players[i]
        dx, dy = dt[d]
        nx, ny = x+dx, y+dy
        # 격자를 벗어나면 정반대 방향으로 방향 바꿔서 1만큼 이동
        if not (0 <= nx < N and 0 <= ny < N):
            nx, ny = x-dx, y-dy
            players[i][2] = (d+2)%4

        # 2-1. 플레이어가 있으면 두 플레이어가 싸우게 됨
        if where[nx][ny]:
            j = where[nx][ny]-1
            winner, loser = None, None
            # 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 승리
            # 수치가 같다면 플레이어 초기 능력치가 높은 플레이어가 승리
            if (s+g > players[j][3]+players[j][4])\
            or (s+g == players[j][3]+players[j][4] and s > players[j][3]):
                winner, loser = i, j
            else:
                winner, loser = j, i
            
            # 이긴 플레이어는 각 플레이어 초기 능력치과 가지고 있는 총의 공격력의 합의 차이만큼 포인트 획득
            x1, y1, d1, s1, g1 = players[winner]
            x2, y2, d2, s2, g2 = players[loser]
            score[winner] += (s1+g1)-(s2+g2)
            where[x1][y1], where[x2][y2] = 0, 0     # 일단 둘이 방향전환할 때 안 걸치적거리게 없애주기

            # 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓는다
            g2 = 0
            matrix[nx][ny].append(players[loser][4])
            players[loser][4] = 0

            matrix[nx][ny].sort()
            # 이긴 플레이어는 승리한 칸에 떨어진 총들과 원래 들고 있던 총 중 공격력이 높은 총 획득하고 나머지 총은 내려놓기
            if matrix[nx][ny] and g1 < matrix[nx][ny][-1]:
                new_gun = matrix[nx][ny].pop()
                if g1: matrix[nx][ny].append(g1)
                players[winner] = [nx,ny,d1,s1,new_gun]
            else: players[winner] = [nx,ny,d1,s1,g1]
            where[nx][ny] = winner+1

            # 진 플레이어는 원래 가던 방향대로 한 칸 이동
            dx, dy = dt[d2]
            nnx, nny = nx+dx, ny+dy

            # 이동하려는 칸에 다른 플레이어가 있거나 격자 밖이라면 오른쪽으로 90도 회전
            while not (0 <= nnx < N and 0 <= nny < N) or where[nnx][nny]:
                d2 = (d2+1)%4
                dx, dy = dt[d2]
                nnx, nny = nx+dx, ny+dy
            # 빈 칸이 보이면 이동
            where[nnx][nny] = loser+1

            # 해당 칸에 총이 있다면 공격력이 더 쎈 총을 획득하고 나머지 총들은 해당 격자에 내려 놓기
            matrix[nnx][nny].sort()
            if matrix[nnx][nny] and g2 < matrix[nnx][nny][-1]:
                new_gun = matrix[nnx][nny].pop()
                if g2: matrix[nnx][nny].append(g2)
                players[loser] = [nnx,nny,d2,s2,new_gun]
            else: players[loser] = [nnx,nny,d2,s2,g2]


        # 2. 이동한 방향에 플레이어 없다면
        else:
            # 해당 칸에 총이 있으면 총 획득
            matrix[nx][ny].sort()
            # 내가 갖고 있는 총이 있으면 플레이어가 가진 총 가운데 공격력이 더 쎈 총을 획득하고
            if matrix[nx][ny] and g < matrix[nx][ny][-1]:
                # 플레이어가 가진 총 가운데 공격력이 더 쎈 총을 획득하고
                # 나머지 총은 해당 격자에 둔다
                players[i][4] = matrix[nx][ny].pop()
                if g: matrix[nx][ny].append(g)
            players[i][0], players[i][1] = nx, ny
            where[x][y], where[nx][ny] = where[nx][ny], where[x][y]

print(*score)

# 2차 풀이
'''
- 1차. 13:56 ~ 15:44 - TC 6번에서 틀림
- 2차. 17:12 갈아엎고 다시 짜자
- 3차. player[lose] = [nx2, ny2, (d2+i)%4, player[lose][3], heappop(matrix[nx2][ny2]+[0])]
- 여기서 matrix[nx2][ny2]에서 바로 줍는게 아니라 새로운 배열에서 주워버려서 지도에 남아버림
'''
from sys import stdin
from collections import deque
from heapq import heappop, heappush
input = stdin.readline

# n은 격자의 크기, m은 플레이어의 수, k는 라운드의 수
N, M, K = map(int, input().split())
matrix = [list(map(lambda x: [] if x == '0' else [-int(x)], input().split())) for _ in range(N)]
where = [[0]*N for _ in range(N)]
dt = ((-1,0),(0,1),(1,0),(0,-1))            # ↑, →, ↓, ←
player = []
for idx in range(1,M+1):
    x, y, d, s = map(int, input().split())  # 위치, 방향, 초기 능력치
    player.append([x-1,y-1,d,s,0])
    where[x-1][y-1] = idx
score = [0]*M
for _ in range(K):
    for me in range(M):
        r, c, d, s, g = player[me]
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy

        # 격자 벗어나는 경우 방향 바꿔 이동
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            d = (d+2)%4
            player[me][2] = d
            nx, ny = r-dx, c-dy

        player[me][0], player[me][1] = nx, ny

        if where[nx][ny]:
            where[r][c] = 0
            other = where[nx][ny]-1
            rr, cc, dd, ss, gg = player[other]

            # 해당 플레이어 초기 능력치과 총의 공격력의 합 비교
            win, lose = None, None
            if s-g > ss-gg: win, lose = me, other
            elif s-g < ss-gg: win, lose = other, me
            elif s > ss: win, lose = me, other
            else: win, lose = other, me

            r1, c1, d1, s1, g1 = player[win]
            r2, c2, d2, s2, g2 = player[lose]
            # 초기 능력치과 공격력의 합의 차이만큼 획득
            score[win] += (s1-g1)-(s2-g2)

            # 진 플레이어 처리
            heappush(matrix[r2][c2], g2)
            player[lose][-1] = 0
            dx, dy = dt[d2]
            nnx, nny = nx+dx, ny+dy
            while not (0 <= nnx < N and 0 <= nny < N) or where[nnx][nny]:
                d2 = (d2+1)%4
                dx, dy = dt[d2]
                nnx, nny = nx+dx, ny+dy
            if not matrix[nnx][nny]:
                player[lose] = [nnx, nny, d2, player[lose][3], 0]
            else:
                player[lose] = [nnx, nny, d2, player[lose][3], heappop(matrix[nnx][nny])]

            # 이긴 플레이어 처리
            # 플레이어가 이미 총을 가지고 있으면 놓여있는 총 중 가장 센거 획득하고 나머지 격자에 둠
            if not matrix[nx][ny]: continue
            gun = heappop(matrix[nx][ny])
            if gun < g1:
                player[win][-1] = gun
                heappush(matrix[nx][ny], g1)
            else:
                player[win][-1] = g1
                heappush(matrix[nx][ny], gun)

            where[r1][c1], where[r2][c2] = 0, 0
            where[nnx][nny], where[nx][ny] = lose+1, win+1

        # 이동 방향에 플레이어 없으면
        else:
            # 총 있으면 총 획득
            where[nx][ny], where[r][c] = where[r][c], where[nx][ny]
            if not matrix[nx][ny]: continue
            gun = heappop(matrix[nx][ny])
            if gun < g:
                player[me] = [nx, ny, d, s, gun]
                heappush(matrix[nx][ny], g)
            else:
                player[me] = [nx, ny, d, s, g]
                heappush(matrix[nx][ny], gun)

print(*score)

# 3차 풀이
N, M, K = map(int, input().split())
A = [list(map(lambda x: [int(x)], input().split())) for _ in range(N)]
dt = ((-1, 0), (0, 1), (1, 0), (0, -1))  # ↑, →, ↓, ←
P = [[0] * N for _ in range(N)]
players = []
for idx in range(1, M + 1):
    x, y, d, s = map(int, input().split())
    P[x - 1][y - 1] = idx
    players.append([x - 1, y - 1, d, s, 0])

score = [0] * M
for _ in range(K):
    for idx in range(M):
        r, c, d, s, g = players[idx]
        dx, dy = dt[d]
        nx, ny = r + dx, c + dy
        if not (0 <= nx < N and 0 <= ny < N):
            d = (d + 2) % 4
            dx, dy = dt[d]
            nx, ny = r + dx, c + dy
            players[idx][2] = d

        # 플레이어가 있으면
        if P[nx][ny]:
            other = P[nx][ny] - 1
            r2, c2, d2, s2, g2 = players[other]
            if s + g > s2 + g2:
                win, lose = idx, other
            elif s + g == s2 + g2:
                if s > s2:
                    win, lose = idx, other
                else:
                    win, lose = other, idx
            else:
                win, lose = other, idx
            r1, c1, d1, s1, g1 = players[win]
            r2, c2, d2, s2, g2 = players[lose]
            score[win] += (s1 + g1) - (s2 + g2)
            P[r1][c1] = P[r2][c2] = 0

            # 진 플레이어
            players[lose][-1] = 0
            A[nx][ny].append(g2)
            for i in range(4):
                dx, dy = dt[(d2 + i) % 4]
                nnx, nny = nx + dx, ny + dy
                if 0 <= nnx < N and 0 <= nny < N and not P[nnx][nny]:
                    P[nnx][nny] = lose + 1
                    mg = 0
                    if A[nnx][nny]:
                        mg = max(A[nnx][nny])
                        A[nnx][nny].remove(mg)
                    players[lose] = [nnx, nny, (d2 + i) % 4, s2, mg]
                    break

            # 이긴 플레이어
            mg = 0
            if g1 < max(A[nx][ny]):
                mg = max(A[nx][ny])
                A[nx][ny].remove(mg)
                A[nx][ny].append(g1)
                players[win][-1] = mg
            P[nx][ny] = win + 1
            players[win] = [nx, ny, d1, s1, max(g1, mg)]

        else:
            mg = 0
            if A[nx][ny]:
                if g < max(A[nx][ny]):
                    mg = max(A[nx][ny])
                    A[nx][ny].remove(mg)
                    A[nx][ny].append(g)
            players[idx] = [nx, ny, d, s, max(g, mg)]
            P[r][c], P[nx][ny] = P[nx][ny], P[r][c]

print(*score)

# 4차 풀이
N, M, K = map(int, input().split())
A = [list(map(lambda x: [int(x)], input().split())) for _ in range(N)]
P = [[0]*N for _ in range(N)]
player = [[]]
for idx in range(1, M+1):
    x, y, d, s = map(int, input().split())
    P[x-1][y-1] = idx
    player.append([x-1, y-1, d, s, 0])
dt = ((-1,0),(0,1),(1,0),(0,-1))
answer = [0]*(M+1)
for k in range(K):
    for m in range(1, M+1):
        r, c, d, s, g = player[m]
        P[r][c] = 0
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        if not (0 <= nx < N and 0 <= ny < N):
            player[m][2] = (d+2)%4
            dx, dy = dt[(d+2)%4]
            nx, ny = r+dx, c+dy
        player[m][0], player[m][1] = nx, ny
        if not P[nx][ny]:
            if A[nx][ny]:
                gun = max(A[nx][ny])
                if gun > g:
                    A[nx][ny].remove(gun)
                    A[nx][ny].append(g)
                    player[m][-1] = gun
            P[nx][ny] = m
        else:
            r2, c2, d2, s2, g2 = player[P[nx][ny]]
            diff, win, lose = -1, -1, -1
            if (s+g) > (s2+g2):
                win, lose = m, P[nx][ny]
                diff = (s+g)-(s2+g2)
            elif (s+g) == (s2+g2):
                if s > s2:
                    win, lose = m, P[nx][ny]
                    diff = (s+g)-(s2+g2)
                else:
                    win, lose = P[nx][ny], m
                    diff = (s2+g2)-(s+g)
            else:
                win, lose = P[nx][ny], m
                diff = (s2+g2)-(s+g)
            answer[win] += diff

            # 진 플레이어
            ng = player[lose][-1]
            A[nx][ny].append(ng)
            player[lose][-1] = 0
            nd = player[lose][2]
            for i in range(4):
                dx, dy = dt[(nd+i)%4]
                rr, cc = nx+dx, ny+dy
                if 0 <= rr < N and 0 <= cc < N:
                    if P[rr][cc]: continue
                else: continue
                player[lose][0], player[lose][1], player[lose][2] = rr, cc, (nd+i)%4
                P[rr][cc] = lose
                if A[rr][cc]:
                    gg = max(A[rr][cc])
                    if gg > 0:
                        A[rr][cc].remove(gg)
                        player[lose][-1] = gg
                break 
                
            # 이긴 플레이어
            ng = player[win][-1]
            gg = max(A[nx][ny])
            if gg > ng:
                A[nx][ny].remove(gg)
                A[nx][ny].append(ng)
                player[win][-1] = gg
            P[nx][ny] = win
        
print(*answer[1:])