# https://www.codetree.ai/training-field/frequent-problems/problems/destroy-the-turret/submissions?page=1&pageSize=20
'''
- 토끼 뛰는거 보니까 낚시왕 물고기 생각나서 포탑 부수러 왔음 (1:18)
- 공격만 잘 하면 나머지는 ㄱㅊ을듯
- 1차 제출: 2:15 테스트케이스 오류
- 2차 제출: 2:18 포탑 정비할 때 턴마다 배열 복사 안했음
- 3차 제출: 2:33 M인데 N이라고 적음!!!!!!!! 무려 3군데나... (352ms, 36mb)
 + 만약 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지됩니다.
 -> 제발 문제 잘 읽자 (문제가 길어서 다 안 읽는 습관 고칠 수 있을까)
'''
from collections import deque

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
new_matrix = [row[:] for row in matrix]

# 포탑 정보 저장
potap = dict()
for r in range(N):
    for c in range(M):
        if matrix[r][c]:
            potap[(r,c)] = [matrix[r][c], 0, r, c]

for turn in range(1,K+1):
    # 1. 공격자 선정
    attack = sorted(potap.values(), key=lambda x: (x[0], -x[1], -(x[2]+x[3]), -x[3]))
    if len(attack) >= 2:
        _, _, er, ec = attack[-1]
    else: break

    attacker = attack[0]
    skill, _, sr, sc = attacker
    new_skill = skill+N+M
    potap[(sr,sc)] = [new_skill, turn, sr, sc]
    matrix[sr][sc] = new_skill

    # 2. 공격자의 공격
    def attack(x,y,skill):
        matrix[x][y] = max(0, matrix[x][y] - skill)
        potap[(x,y)][0] = matrix[x][y]
        if not potap[(x,y)][0]: del potap[(x,y)]

    # (1) 레이저 공격
    def bfs(x,y):
        visited = [[False]*M for _ in range(N)]
        queue = deque([[(x,y)]])
        visited[x][y] = True

        while queue:
            arr = queue.popleft()
            r, c = arr[-1]

            if (r,c) == (er,ec):
                for x, y in arr[1:-1]:
                    attack(x,y,new_skill//2)
                x, y = arr[-1]
                attack(x,y,new_skill)
                return True

            for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
                nx, ny = (r+dx)%N, (c+dy)%M
                if not visited[nx][ny] and matrix[nx][ny]:
                    visited[nx][ny] = True
                    queue.append(arr+[(nx,ny)])

        return False

    if not bfs(sr, sc):
        # (2) 포탄 공격
        for dx, dy in ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)):
            nr, nc = (er+dx)%N, (ec+dy)%M
            if (sr, sc) == (nr, nc): continue
            if matrix[nr][nc]: attack(nr,nc,new_skill//2)
        attack(er,ec,new_skill)

    # 3. 포탑 부서짐 -> 공격하면서 함께 처리했음
    # 4. 포탑 정비
    for r in range(N):
        for c in range(M):
            if (r,c) == (sr,sc) or (r,c) == (er,ec): continue
            if matrix[r][c] and matrix[r][c] == new_matrix[r][c]:
                matrix[r][c] += 1
                potap[(r,c)][0] += 1

    new_matrix = [row[:] for row in matrix]

print(max(map(max, matrix)))