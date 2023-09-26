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