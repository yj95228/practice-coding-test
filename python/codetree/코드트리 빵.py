# https://www.codetree.ai/training-field/frequent-problems/problems/codetree-mon-bread/description?page=1&pageSize=20
'''
- 어떻게 접근할지 감이 안 잡혀서 설계 하고 풀기 시작한게 20분쯤..
- 짜고 나니까 왜 13:56이지... 불안하다
- TC가 별로 없어서 일단 제출해봐야겠다
- 13:57 역시 TC 5번에서 틀림... -> 손으로 풀어도 8 나오는데 어떻게 7 나오지
- 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.를 놓쳤긴 했는데
  이거 고려해도 모르겠다
- 문제를 잘 못 이해한것 같음
- 베이스캠프를 먼저 찾고 편의점을 찾았는데 1,2,3 순서대로 했어야함
- 갈아엎자 14:40
- visited[nx][ny][idx] <= time+1 로 고치니까 맞긴한데 왜 맞지...?
    - 벽 부수고 이동하기 다시 풀어야겠다
- 15:28 TC98에서 메모리 초과남....
- 16:47 TC 맞으니까 일단 제출...
'''
import sys
from heapq import heappop, heappush
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
gs25 = []
visited = [[[0]*M for _ in range(N)] for _ in range(N)]
for idx in range(M):
    X, Y = map(lambda x: int(x)-1, input().split())
    gs25.append([X, Y])
basecamp = [[] for _ in range(M)]
queue = [tuple([i+1, i] + x[:]) for i,x in enumerate(gs25)]
base_find = [False]*M
gs25_find = [0]*M
base_visited = [[[0]*M for _ in range(N)] for _ in range(N)]

def find_basecamp(x,y,i):
    global basecamp, base_visited
    base_visited2 = [[v[:] for v in row] for row in base_visited]
    queue = deque([(i+1, x,y)])
    base_visited2[x][y][i] = i+1
    while queue:
        for _ in range(len(queue)):
            time, r, c = queue.popleft()
            if matrix[r][c] == 1:
                basecamp[i].append((r,c))
            for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not base_visited2[nx][ny][idx]:
                    base_visited2[nx][ny][idx] = i+1
                    heappush(queue, (time+1, nx, ny))
        if basecamp[i]:
            r, c = min(basecamp[i])
            for m in range(M):
                base_visited[r][c][m] = i+1
            return r, c

while queue:
    time, idx, r, c = heappop(queue)

    # 베이스캠프 찾기
    if idx+1 == time and not base_find[idx]:
        r, c = find_basecamp(r,c,idx)
        base_find[idx] = True
        heappush(queue, (idx+1, idx, r, c))

    # 편의점 이미 찾았음
    if gs25_find[idx]: continue

    # 편의점 찾기
    elif gs25[idx] == [r,c]:
        gs25_find[idx] = time
        for m in range(M):
            base_visited[r][c][m] = time

    for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
        nx, ny = r+dx, c+dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny][idx]\
        and (not base_visited[nx][ny][idx] or time <= base_visited[nx][ny][idx]):

            visited[nx][ny][idx] = True
            heappush(queue, (time+1, idx, nx, ny))


# # 2. 편의점 도착하면 멈추고 다른 사람들은 해당 편의점 칸을 지나갈 수 X
# # 3. 현재 시간이 t분이고 t <= m을 만족한다면 t번 사람은 편의점과 가장 가까운 베이스 캠프 들어감
print(max(gs25_find))