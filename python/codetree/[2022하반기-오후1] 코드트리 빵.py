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


# 두번째 풀이
def find_base(x,y):
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    queue = deque([(x,y)])
    basecamp = []
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if matrix[r][c] == '1':
                basecamp.append((r,c))
            for dx, dy in ((-1,0),(0,-1),(0,1),(1,0)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not cant_go[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
        if basecamp:
            return min(basecamp)

def bfs(x,y,m):
    visited = [[None]*N for _ in range(N)]
    visited[x][y] = (-1,-1)
    queue = deque([(x,y)])
    while queue:
        r, c = queue.popleft()
        if (r,c) == cvs[m]:
            while visited[r][c]:
                if visited[r][c] == (x,y):
                    return r, c
                r, c = visited[r][c]
            
        for dx, dy in ((-1,0),(0,-1),(0,1),(1,0)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not cant_go[nx][ny]:
                visited[nx][ny] = (r,c)
                queue.append((nx,ny))

N, M = map(int, input().split())
matrix = [input().split() for _ in range(N)]
cvs = []
where = []
for _ in range(M):
    X, Y = map(lambda x: int(x)-1, input().split())
    cvs.append((X,Y))
cant_go = [[False]*N for _ in range(N)]
find = [0]*M
time = 0
while True:
    tmp = []
    for m in range(M):
        if find[m]: continue

        # 격자에 있는 사람들 모두 편의점 방향을 향해 1칸 움직인다
        if m < len(where):
            r, c = where[m]
            bfs(r,c,m)
            nx, ny = bfs(r,c,m)
            where[m] = [nx, ny]
            if (nx, ny) == cvs[m]:
                tmp.append((nx, ny))   
                find[m] = time+1

    if all(find):
        print(max(find))
        break

    # 편의점에 도착하면 편의점에서 멈추고 지나갈 수 없어짐
    # 단 격자에 있는 사람들이 모두 이동한 후 지나갈 수 없어짐
    if tmp:
        for r, c in tmp:
            cant_go[r][c] = True

    # 현재 시간이 t분이고 t <= m를 만족하면 편의점과 가장 가까이 있는 베이스캠프 간다
    if time <= m:
        r, c = cvs[time]
        br, bc = find_base(r,c)
        where.append([br,bc])
        cant_go[br][bc] = True

    time += 1

# 3차 풀이
import sys
from collections import deque

input = sys.stdin.readline


def go_basecamp(who, x, y):
    q = [(x, y)]
    visited = [[e[who] for e in row] for row in V]
    visited[x][y] = 1
    while q:
        next_q = []
        s = set()
        for r, c in q:
            if A[r][c]:
                s.add((r, c))
            for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    next_q.append((nx, ny))
        if s: return min(s)
        q = next_q


def bfs(x, y, who):
    er, ec = cvs[who]
    visited = [[e[who] for e in row] for row in V]
    q = [(x, y)]
    visited[x][y] = 1
    dist = 0
    while q:
        next_q = []
        for r, c in q:
            if (r, c) == (er, ec): return dist
            for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    next_q.append((nx, ny))
        q = next_q
        dist += 1


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cvs, queue = [], deque()
for t in range(1, M + 1):
    x, y = map(lambda x: int(x) - 1, input().split())
    queue.append((t - 1, x, y))
    cvs.append((x, y))

base, arrive = [0] * M, [0] * M
V = [[[0] * M for _ in range(N)] for _ in range(N)]
time = 1
while queue:
    visited = set()
    for _ in range(len(queue)):
        who, r, c = queue.popleft()

        # 아직 시간 안 됐으면 그대로 다시 queue에 넣기
        if time < who + 1:
            queue.append((who, r, c))
            continue

        # 이미 도착한 사람은 더 이상 가지 않아도 됨
        elif arrive[who]:
            continue

        # t <= m이면 편의점에서 가장 가까운 베이스캠프 가기
        elif not base[who] and time == who + 1:
            r, c = go_basecamp(who, r, c)
            base[who] = 1
            visited.add((r, c))

        s = set()
        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nx, ny = r + dx, c + dy
            if 0 <= nx < N and 0 <= ny < N and (not V[nx][ny][who] or time <= V[nx][ny][who]):
                dist = bfs(nx, ny, who)
                if dist is not None: s.add((dist, nx, ny))

        if s:
            dist, nx, ny = min(s)
            if dist:
                V[nx][ny][who] = time + 1
                queue.append((who, nx, ny))

            # 편의점 도착
            else:
                arrive[who] = time + 1
                visited.add((nx, ny))
                continue

    for r, c in visited:
        for m in range(M):
            V[r][c][m] = time

    time += 1

print(max(arrive))

# 4차 풀이
def bfs(r, c, er, ec):
    V = [row[:] for row in cant]
    V[r][c] = 1
    queue = [(r, c)]
    dist = 0
    while queue:
        next_q = []
        for r, c in queue:
            if (r, c) == (er, ec): return dist
            for dx, dy in ((-1,0),(0,-1),(0,1),(1,0)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not V[nx][ny]:
                    V[nx][ny] = 1
                    next_q.append((nx, ny))
        queue = next_q
        dist += 1
    return 987654321


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
conv = [[]]
for _ in range(M):
    r, c = map(lambda x: int(x)-1, input().split())
    conv.append((r, c))
player = [[]]
answer = [1] + [0]*M
time = 1
cant = [[0]*N for _ in range(N)]
while True:
    if 0 not in answer: break
    
    cant_list = []
    for m in range(1, M+1):
        # 1. ↑, ←, →, ↓ 의 우선 순위로 편의점 최단거리 향해 움직이기
        if m < len(player):
            if answer[m]: continue
            r, c = player[m]
            er, ec = conv[m]
            rr, cc, mn = -1, -1, 987654321
            for dx, dy in ((-1,0),(0,-1),(0,1),(1,0)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and not cant[nx][ny]:
                    mm = bfs(nx, ny, er, ec)
                    if mm < mn:
                        rr, cc, mn = nx, ny, mm
            if mn != 987654321: player[m] = [rr, cc]
            if (rr, cc) == (er, ec):
                cant_list.append((rr, cc))
                answer[m] = time
    for r, c in cant_list:
        cant[r][c] = 1
    
    if time <= M:
        r, c = conv[time]
        basecamp = []
        queue = [(r, c)]
        V = [row[:] for row in cant]
        V[r][c] = 1
        while queue:
            next_q = []
            for r, c in queue:
                if A[r][c]: basecamp.append((r, c))
                for dx, dy in ((-1,0),(0,-1),(0,1),(1,0)):
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < N and 0 <= ny < N and not V[nx][ny]:
                        V[nx][ny] = 1
                        next_q.append((nx, ny))
            if basecamp:
                rr, cc = min(basecamp)
                player.append([rr, cc])
                cant[rr][cc] = 1
                break
            queue = next_q
    time += 1
print(max(answer))