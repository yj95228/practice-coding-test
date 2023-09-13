# 1차 제출: 실패 (소요시간 55분)
# - 연합 번호 다는 것과 인구 이동할 때 visited 배열을 언제 정의할지가 헷갈렸음
# - 인구 이동 가능한지 종료 조건을 어떻게 정의할지 어려웠음
# - 단순히 BFS 써도 되는데 인접한지만 보면 되니까 deque을 import하지 않고 실행 속도를 고려하여
# - stack을 활용한 DFS를 써야겠다고 생각했다가 중간에 deque 썼다가 다시 제자리로 돌아옴
# 2차 제출: (소요시간 80분) 연합 번호 다는거 cnt += 1을 안 해줌.... (126172kb, 1048ms)
# 3차 제출: BFS 쓰면 더 빠른지 확인 (1048ms -> 2640ms)
# 4차 제출: if문 안에 조건 두개라서 순서 변경 (1048ms -> 868ms)
# https://www.acmicpc.net/problem/16234

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, L, R = map(int, input().split())
matrix = [[999]*(N+2)] + [[999] + list(map(int, input().split())) + [999] for _ in range(N)] + [[999]*(N+2)]
answer, cnt = 0, 1

while True:
    can_move = False                                # 인구 이동 가능한지
    country = [[0]*(N+2) for _ in range(N+2)]       # 연합 나라 번호
    new_matrix = [row[:] for row in matrix]         # 연합 인구
    visited = [[False]*(N+2) for _ in range(N+2)]   # 연합할 때 쓸 visited 배열

    # 국경선 공유하기
    for r in range(1,N+1):
        for c in range(1,N+1):
            # 이미 나라가 정해졌다면 탐색 X
            if country[r][c]: continue
            # 연합의 인구 수, 연합을 이루고 있는 칸의 갯수
            result, length = matrix[r][c], 1

            # 연합 번호 달기
            stack = [(r,c)]
            country[r][c] = cnt
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if L <= abs(matrix[x][y] - matrix[nx][ny]) <= R and not country[nx][ny]:
                        can_move = True
                        country[nx][ny] = cnt
                        result += matrix[nx][ny]
                        length += 1
                        stack.append((nx,ny))
            cnt += 1

            # 인구 이동
            same = country[r][c]
            stack = [(r,c)]
            visited[r][c] = True
            while stack:
                x, y = stack.pop()
                new_matrix[x][y] = result//length
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if country[nx][ny] == same and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx,ny))
    if can_move:
        answer += 1
    else:
        break
    matrix = new_matrix

print(answer)