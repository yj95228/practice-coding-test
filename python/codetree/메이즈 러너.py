'''
- 소요시간 : 5시간 (173ms, 30MB)
- 어려웠던 점 (사실 쉬운게 하나도 없어서 전부 다..)
    - 출구까지 가까운 방향으로 움직이기
        - 참가자마다 4방향으로 가게 될 경우 출구까지의 목적지와의 거리를 보는 것도 방법이었을듯 (from 유나님)
    - 가장 작은 정사각형 찾기
        - 참가자마다 정사각형 그려보고 가장 우선순위인 정사각형으로 보는 방법 (from 유나님)
    - 범위가 정해진 시계방향 90도 회전하기
        - 해당 범위의 배열만 떼내서 90도 회전시킨 후 다시 대입시키는 방법 (from 성환님)
    - 한 칸에 여러 모험가가 있을 수 있다는 것을 간과함 (from TC)
'''
# https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/description?page=1&pageSize=20
N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
runner = []
exit, answer = M, 0
for i in range(1,M+1):
    A, B = map(lambda x: int(x)-1, input().split())
    runner.append([A,B])
er, ec = map(lambda x: int(x)-1, input().split())
matrix[er][ec] = -1

for _ in range(1,K+1):
    new_matrix = [row[:] for row in matrix]

    # 모든 참가자는 한칸씩 움직인다
    # 출구까지의 최단 거리가 가까운 쪽으로 (상하로 움직이는 것을 우선)
    for who in range(M):
        r, c = runner[who]
        if (r,c) == (None, None): continue
        if 0 <= r-1 and r > er and matrix[r-1][c] <= 0:
            answer += 1
            if matrix[r-1][c] == -1:
                exit -= 1
                runner[who] = [None, None]
            else:
                runner[who] = [r-1, c]
        elif r+1 < N and r < er and matrix[r+1][c] <= 0:
            answer += 1
            if matrix[r+1][c] == -1:
                exit -= 1
                runner[who] = [None, None]
            else:
                runner[who] = [r+1, c]
        elif 0 <= c-1 and c > ec and matrix[r][c-1] <= 0:
            answer += 1
            if matrix[r][c-1] == -1:
                exit -= 1
                runner[who] = [None, None]
            else:
                runner[who] = [r, c-1]
        elif c+1 < N and c < ec and matrix[r][c+1] <= 0:
            answer += 1
            if matrix[r][c+1] == -1:
                exit -= 1
                runner[who] = [None, None]
            else:
                runner[who] = [r, c+1]

    if exit == 0: break

    # 미로 회전 위한 가장 작은 정사각형 만들기
    flag, sr1, sc1, sr2, sc2 = False, None, None, None, None
    visited = [[False]*N for _ in range(N)]
    for i in range(1,N):
        for x in range(er-i,er+1):
            for y in range(ec-i, ec+1):
                if not (0 <= x and 0 <= y and x+i < N and y+i < N): continue
                for z1 in range(i+1):
                    for z2 in range(i+1):
                        if flag: break
                        nx, ny = x+z1, y+z2
                        if visited[nx][ny]: continue
                        else:
                            visited[nx][ny] = True
                            for r, c in runner:
                                if flag: break
                                elif (r,c) == (None, None): continue

                                if (r,c) == (nx,ny):
                                    sr1, sc1, sr2, sc2 = x, y, x+i, y+i
                                    flag = True
                                    break

                    if flag: break
                if flag: break
            if flag: break
        if flag: break

    # 배열 회전시킬 부분 뽑아서 rotate를 dictionary로 처리
    rotate = {(sr1+r, sc1+c): (sr1+c, sc2-r) for r in range(i+1) for c in range(i+1)}
    
    # 미로 회전시키기
    for k, v in rotate.items():
        r1, c1 = k
        r2, c2 = v
        if matrix[r1][c1] > 0:
            new_matrix[r2][c2] = matrix[r1][c1]-1
        else:
            if matrix[r1][c1] == -1:    # 탈출구 회전시키기
                er, ec = r2, c2
            new_matrix[r2][c2] = matrix[r1][c1]

    # 모험가 회전시키기
    for m in range(len(runner)):
        r, c = runner[m]
        if (r,c) in rotate:
            r2, c2 = rotate[(r,c)]
            runner[m] = [r2, c2]

    matrix = new_matrix
    if exit == 0: break

print(answer)
print(er+1, ec+1)