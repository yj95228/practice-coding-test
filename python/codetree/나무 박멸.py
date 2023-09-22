# https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all/submissions?page=1&pageSize=20
'''
- 나무박멸이 나무 재테크 느낌나서 나무박멸 먼저 풀기로 함 (1:06)
- 풀면서 수정한 것들
    - 대각선 탐색하면서 중간 나무 박멸 처리 안 함
    - 벽도 박멸한 나무 그루 수로 계산함
    - nx, ny = r+dx, c+dy 빼먹어서 저번 statement의 nx, ny를 계산해주고 있었음
    - (헷갈린 것) 제초제 사라지게 하는 것을 언제 처리할지
- 1차. (13:47) 제초제 뿌릴 곳을 못 찾을 경우를 고려하지 않아 런타임 에러
- 2차. (13:49) 제초제를 나무 없는 칸에도 뿌릴 수 있지 않을까 해서 해당 조건 수정
-> 만약 박멸시키는 나무의 수가 동일한 칸이 있는 경우에는 행이 작은 순서대로, 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됩니다.
-> 박멸시킬 곳이 없다면 default로 가장 첫번째 행과 첫번째 열에 제초제 (벽이거나 빈 칸이어도 제초제 놓을 수 있으므로)
- 3차. (14:17, 226ms, 31MB) 벽에 제초제 뿌리면서 벽을 없애버렸음....
'''
import sys
sys.stdin = open('input.txt','r')

N, M, K, C = map(int, input().split())
matrix = [[-1]*(N+2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1]*(N+2)]
destroy = [[0]*(N+2) for _ in range(N+2)]
answer = 0

for _ in range(M):

    print('0.시작')
    for row in matrix:
        for x in row:
            print(f'{x:3d}', end='')
        print()

    # 1. 인접한 4개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장
    new_matrix = [row[:] for row in matrix]
    for r in range(1,N+1):
        for c in range(1,N+1):
            if matrix[r][c] > 0:
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if matrix[nx][ny] > 0:
                        new_matrix[r][c] += 1
    matrix = new_matrix
    new_matrix = [row[:] for row in matrix]

    print('1.성장')
    for row in matrix:
        for x in row:
            print(f'{x:3d}', end='')
        print()

    # 2. 나무의 인접한 4개 칸 중 벽, 다른 나무, 제초케 모두 없는 칸에 번식
    # -> (나무 그루 수)/(번식 가능한 칸 개수)
    for r in range(1,N+1):
        for c in range(1,N+1):
            if matrix[r][c] > 0:
                cnt = 0
                grow = set()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if matrix[nx][ny] == 0 and not destroy[nx][ny]:
                        cnt += 1
                        grow.add((nx,ny))
                if cnt:
                    for rr, cc in grow:
                        new_matrix[rr][cc] += matrix[r][c]//cnt

    matrix = new_matrix

    print('2.번식')
    for row in new_matrix:
        for x in row:
            print(f'{x:3d}', end='')
        print()

    # 해가 바뀔 때마다 제초제 지속력 떨어짐
    for r in range(N+2):
        for c in range(N+2):
            if destroy[r][c] > 0:
                destroy[r][c] -= 1

    print('0.제초제')
    for row in destroy:
        for x in row:
            print(f'{x:3d}', end='')
        print()

    # 3. 제초제 뿌리면 나무가 가장 많이 박멸되는 칸에 제초제를 뿌림
    # - 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 X
    # - 나무가 있는 칸에 제초제를 뿌리면 4개의 대각선 방향으로 K칸만큼 전파
    # - 전파되는 도중 벽이 있거나 나무가 아예 없는 칸이 있으면 그 칸까지만 제초제가 뿌려짐
    # - 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라짐
    # - 제초제가 뿌려진 곳에 다시 제초제가 뿌려지면 새로 뿌려진 해로부터 다시 c년동안 제초제 유지
    rr, cc, mx = 1, 1, -1
    for r in range(1,N+1):
        for c in range(1,N+1):
            result = matrix[r][c] if matrix[r][c] > 0 else 0
            if matrix[r][c] > 0:
                for dx, dy in ((1,1),(1,-1),(-1,1),(-1,-1)):
                    for k in range(1,K+1):
                        nx, ny = r+k*dx, c+k*dy
                        if matrix[nx][ny] > 0:
                            result += matrix[nx][ny]
                        else: break
            if mx < result:
                rr, cc, mx = r, c, result

    destroy[rr][cc] = C
    if matrix[rr][cc] > 0:
        answer += matrix[rr][cc]
        matrix[rr][cc] = 0
        for dx, dy in ((1,1),(1,-1),(-1,1),(-1,-1)):
            for k in range(1,K+1):
                nx, ny = rr+k*dx, cc+k*dy
                if 1 <= nx <= N and 1 <= ny <= N:
                    destroy[nx][ny] = C
                    if matrix[nx][ny] > 0:
                        answer += matrix[nx][ny]
                        matrix[nx][ny] = 0
                    else: break
                else: break

    print('3.제초작업')
    for row in new_matrix:
        for x in row:
            print(f'{x:3d}', end='')
        print()
    print('3.제초제')
    for row in destroy:
        for x in row:
            print(f'{x:3d}', end='')
        print()
    print('4.정답',answer)