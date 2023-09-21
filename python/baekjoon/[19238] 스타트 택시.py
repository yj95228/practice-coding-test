# https://www.acmicpc.net/problem/19238
'''
- 상어 움직이는거 너무 정신없어서 택시 태우러 옴 (09:05)
- 09:28 코드 다 짜고 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우 반례 만들어보고 09:39 제출
- 1차 제출: 틀렸습니다 (6%)
- 2차 제출: 승객 출발지-도착지 사이에 벽 있어서 못 내려주는 경우 -1
- 3차 제출: (-1,0),(0,-1),(0,1),(1,0) 순으로 큐에 넣는 방식말고 그냥 같은 거리 다 보고 행, 열 작은걸로 처리
- 4차 제출: 승객 출발지-도착지 벽을 생각 못하고 그냥 절대값 거리로 계산하는 실수함........ ㅇㅁㅇ릐ㅏㄴㅇ라ㅓ니
- 5차 제출: 시간 얼마 안 남아서 일단 제출 (117264kb 204mb)
    - min에 key값 넣은거랑 end 반환값이 -1일 때 조건 두가지 넣어준거 차이인데
      성진님께 여쭤보니 tuple을 min/max하면 기본적으로 첫번째, 두번째 ... 값으로 정렬한다고 하니
      후자 조건 때문에 통과한 것 같음
'''
import sys
from collections import deque
input = sys.stdin.readline

# 승객 출발지 -> 도착지까지의 거리
def end(x,y):
    queue = deque([(x,y,0)])
    visited = [[False]*(N+2) for _ in range(N+2)]
    visited[x][y] = True
    er, ec = target[matrix[x][y]]
    while queue:
        r, c, d = queue.popleft()
        if (r,c) == (er,ec): return d
        for dx, dy in ((-1,0),(0,-1),(0,1),(1,0)):  # ^ < > v
            nx, ny = r+dx, c+dy
            if not visited[nx][ny] and matrix[nx][ny] != -1:
                visited[nx][ny] = True
                queue.append((nx,ny,d+1))
    return -1

# 택시 운전해서 손님 태워서 내리기
def start(x,y,k):
    global sr, sc, M, K
    queue = deque([(x,y,k)])
    visited = [[False]*(N+2) for _ in range(N+2)]
    visited[x][y] = True

    while queue:
        same_distance = []
        for _ in range(len(queue)):
            r, c, oil = queue.popleft()

            if matrix[r][c]: same_distance.append((r,c,oil))    # 출발지
            elif oil < 0: return -1                             # 연료 없으면

            for dx, dy in ((-1,0),(0,-1),(0,1),(1,0)):  # ^ < > v
                nx, ny = r+dx, c+dy
                if not visited[nx][ny] and matrix[nx][ny] != -1:
                    visited[nx][ny] = True
                    queue.append((nx,ny,oil-1))

        if same_distance:
            r, c, oil = min(same_distance, key=lambda x: (x[0], x[1]))
            er, ec = target[matrix[r][c]]
            distance = end(r,c)
            if distance == -1: return -1                # 도착지까지 못 태워주면 -1
            elif oil < distance: return -1              # 도착지까지 연료 부족하면 -1
            matrix[r][c] = 0                            # 승객 태워서
            M -= 1                                      # 내려주기
            sr, sc = er, ec                             # 도착지로 택시 위치 옮기기
            return oil+distance

    return -1   # 큐를 다 돌았는데도 손님을 못 만나면

N, M, K = map(int, input().split())
matrix = [[-1]*(N+2)] +\
         [[-1] + list(map(lambda x: -1 if x == '1' else 0, input().split())) + [-1] for _ in range(N)] +\
         [[-1]*(N+2)]
sr, sc = map(int, input().split())
target = [[] for _ in range(M+1)]
for i in range(1,M+1):
    A, B, C, D = map(int, input().split())
    matrix[A][B] = i
    target[i] = [C,D]

while M:
    K = start(sr, sc, K)
    if K == -1:
        print(-1)
        break
else:
    print(K)