'''
- 처음에 팀별로 머리/나머지/꼬리 보관해둬야하나 생각했는데 그냥 전체 팀 총합을 구하면 되는걸 보고
  시키는대로 움직이게만 하면 되겠다고 생각함
  - 어떤 걸 구하는건지 먼저 보자
- for r for c 에서 머리사람 옮겨 놓고 또 다음 for문 돌아버림... 메이즈 러너와 같은 실수
  - 머리 사람만 따로 구해놓자
- 15:30 다 짠듯
- 코드트리에서 임의의 TC 넣으면 맞는지 확인해주는 기능을 활용해봄
  - K = 3으로 바꿔봤는데 메모리 초과....??
  - 15:46 DFS에서 if not visited 안 넣음...
  - K = 10에서 답이 달라서 확인해보니 라운드 정보가 달랐음
  - K를 늘리니까 시간초과 떠서 하나하나 움직이는게 아니고 머리사람과 꼬리사람만 움직여줘야겠다...
    - 다행히 머리사람으로 꼬리사람 잡는 함수가 있어서 그걸 활용해야겠다고 생각함
      - 그래도 시간초과
    - 머리사람으로 꼬리사람 찾을 수 있게 미리 저장해둬야겠다
    - break 아까 걸었다가 함수로 빼고 나서 break를 빼먹었네
  - (16:32) TC로 준 예제 K = 1000도 이제는 잘 돌아가니까 제출해보자
  - TC 4번 머리와 꼬리가 연결된 경우 고려 못 했네
    - (16:48) 고쳤더니 코드가 너무 더러워졌지만 TC 맞고 시간 없으니까 일단 제출
  - TC 5번 점수 계산할 때 꼬리에서 머리로 바로 가버림 (17:18 제출)
  - TC 9번 머리랑 꼬리가 연결된 경우 flag 변수를 머리마다 선언해야하는데 밖에 선언함 (17:27 제출)
  - 다른 사람 코드 보니 사람들 배열과 방향을 저장해두고 이동시키는 방식을 활용하는 게 좋아보임
'''
def head_to_tail(x,y):
    visited = [[False]*(N+2) for _ in range(N+2)]
    visited[x][y] = True
    stack = [(x,y)]
    while stack:
        r, c = stack.pop()
        if matrix[r][c] == 3:
            return r,c
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if not visited[nx][ny] and (matrix[nx][ny] == 2 or matrix[nx][ny] == 3):
                visited[nx][ny] = True
                stack.append((nx,ny))

# 머리와 꼬리 바꿔주고 점수 return
def to_head(x,y):
    visited = [[False]*(N+2) for _ in range(N+2)]
    visited[x][y] = True
    stack = [(x,y,1)]
    while stack:
        r, c, score = stack.pop()
        if matrix[r][c] == 1:
            tr, tc = new_tail[(r,c)]
            matrix[tr][tc], matrix[r][c] = matrix[r][c], matrix[tr][tc]
            return score
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if not visited[nx][ny] and (matrix[nx][ny] == 1 or matrix[nx][ny] == 2):
                visited[nx][ny] = True
                stack.append((nx,ny,score+1))

N, M, K = map(int, input().split())
matrix = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
answer = 0

# 라운드 정보 미리 저장
rounds = []
for r in range(1,N+1):
    round = []
    for c in range(1,N+1):
        round.append((r,c))
    rounds.append(round)
for c in range(1,N+1):
    round = []
    for r in range(N,0,-1):
        round.append((r,c))
    rounds.append(round)
for r in range(N,0,-1):
    round = []
    for c in range(N,0,-1):
        round.append((r,c))
    rounds.append(round)
for c in range(N,0,-1):
    round = []
    for r in range(1,N+1):
        round.append((r,c))
    rounds.append(round)

for k in range(K):
    # 머리 사람 찾기
    tail = dict()
    for r in range(1,N+1):
        for c in range(1,N+1):
            if matrix[r][c] == 1:
                tail[(r,c)] = head_to_tail(r,c)

    # 1. 머리사람을 따라서 한칸 이동
    new_tail = dict()
    for r, c in tail:   # 이름은 tail이지만 머리사람임
        rotate = False
        tr, tc = tail[(r,c)]
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            if rotate: break
            nx, ny = r+dx, c+dy
            if matrix[nx][ny] == 4:
                matrix[nx][ny], matrix[r][c] = 1, 2
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nr, nc = tr+dx, tc+dy
                    if matrix[nr][nc] == 2:
                        new_tail[(nx,ny)] = (nr,nc)
                        matrix[nr][nc], matrix[tr][tc] = 3, 4
                        break
                break
            elif (nx,ny) == (tr,tc):
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nr, nc = tr+dx, tc+dy
                    if matrix[nr][nc] == 2:
                        matrix[r][c], matrix[tr][tc], matrix[nr][nc] = 2, 1, 3
                        new_tail[(tr,tc)] = (nr,nc)
                        rotate = True
                        break

    # 2. 각 라운드마다 공이 정해진 선을 따라 던져진다 (오른쪽 / 위 / 왼쪽 / 아래)
    # - 4n번째 라운드 넘어가면 다시 1번째 라운드 방향으로 돌아간다
    # 3. 공이 던져질 경우에 선에 사람이 있으면 최초에 만나는 사람이 공을 얻어 k번째 사람이면 k**2 점수 얻음
    # - 공을 획득한 팀의 경우 방향이 바뀜
    now = k%(4*N)
    find = False
    for r, c in rounds[now]:
        if matrix[r][c] == 1:
            answer += 1
            tr, tc = new_tail[(r,c)]
            matrix[tr][tc], matrix[r][c] = matrix[r][c], matrix[tr][tc]
            break
        elif matrix[r][c] == 2:
            answer += to_head(r,c)**2
            break
        elif matrix[r][c] == 3:
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if matrix[nx][ny] == 2:
                    answer += (to_head(nx,ny)+1)**2
                    find = True
                    break
            if find: break

print(answer)

# 2차 풀이
'''
- 1차. 11:02 ~ 13:08 (점심시간 포함) -> TC 4번에서 틀림
- 다른 사람 코드 많이 볼걸 그랬다 근데 코드트리라 너무 보기 힘드렁
- 2차. 공 잡은 사람 idx가 머리사람 idx보다 클 경우 따로 처리
- 저번에는 머리에서 꼬리로 dfs로 찾아가는 방식이라면 이번에는 idx 저장하는 방식으로 짬
TODO: 다음에는 꼬리 pop 다음 경로 append 해보자
'''
def dfs(x,y):
    visited[x][y] = 1
    stack = [(x,y,3)]
    while stack:
        r, c, who = stack.pop()
        if who == 1: head.append((r,c))
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if who == 3 and matrix[nx][ny] == 2:
                    visited[nx][ny] = 1
                    graph[-1].append((nx,ny))
                    stack.append((nx,ny,2))
                elif who == 2 and (matrix[nx][ny] == 2 or matrix[nx][ny] == 1):
                    visited[nx][ny] = 1
                    graph[-1].append((nx,ny))
                    stack.append((nx,ny,matrix[nx][ny]))
                elif (who == 1 or who == 4) and (matrix[nx][ny] == 4 or matrix[nx][ny] == 3):
                    visited[nx][ny] = 1
                    graph[-1].append((nx,ny))
                    stack.append((nx,ny,matrix[nx][ny]))

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 라운드 정보
rounds = []
for r in range(N):
    round = []
    for c in range(N):
        round.append((r,c))
    rounds.append(round)
for c in range(N):
    round = []
    for r in range(N-1,-1,-1):
        round.append((r,c))
    rounds.append(round)
for r in range(N-1,-1,-1):
    round = []
    for c in range(N-1,-1,-1):
        round.append((r,c))
    rounds.append(round)
for c in range(N-1,-1,-1):
    round = []
    for r in range(N):
        round.append((r,c))
    rounds.append(round)
answer, round = 0, 0

# 경로, 머리사람, 꼬리사람 찾기
visited = [[0]*N for _ in range(N)]
graph = []
head, tail = [], []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 3:
            graph.append([(r,c)])
            tail.append((r,c))
            dfs(r,c)

team = len(graph)
for _ in range(K):
    # 이동하기
    for i in range(team):
        length = len(graph[i])
        
        # 꼬리 이동
        idx = graph[i].index(tail[i])
        r, c = graph[i][idx]
        nx, ny = graph[i][(idx+1)%length]
        matrix[nx][ny], matrix[r][c] = 3, 4
        tail[i] = (nx,ny)
        # 머리 이동
        idx = graph[i].index(head[i])
        r, c = graph[i][idx]
        nx, ny = graph[i][(idx+1)%length]
        matrix[nx][ny], matrix[r][c] = 1, 2
        head[i] = (nx,ny)

    # 공 던지기
    catch = False
    for r, c in rounds[round]:
        if catch: break
        if matrix[r][c] == 1 or matrix[r][c] == 2 or matrix[r][c] == 3:
            for i in range(team):
                if (r,c) in graph[i]:
                    here, head_idx = graph[i].index((r,c)), graph[i].index(head[i])
                    if head_idx >= here:
                        answer += (head_idx-here+1)**2
                    else:
                        answer += (head_idx+len(graph[i])-here+1)**2
                    matrix[head[i][0]][head[i][1]] = 3
                    matrix[tail[i][0]][tail[i][1]] = 1
                    head[i], tail[i] = tail[i], head[i]
                    graph[i].reverse()
                    catch = True
                    break
    round = (round+1)%(4*N)
print(answer)

# 3차 풀이
def dfs(x, y, idx):
    stack = [(1, x, y)]
    lst = [(x, y)]
    cnt = 1
    while stack:
        num, r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not V[nx][ny]:
                if num == 1 and A[nx][ny] == 2:
                    stack.append((2, nx, ny))
                    lst.append((nx, ny))
                    cnt += 1
                elif num == 2 and A[nx][ny] in (2,3):
                    stack.append((A[nx][ny], nx, ny))
                    lst.append((nx, ny))
                    cnt += 1
                elif num in (3,4) and A[nx][ny] in (4,1):
                    stack.append((A[nx][ny], nx, ny))
                    lst.append((nx, ny))
                else: continue
                V[nx][ny] = idx
                if A[nx][ny] == 1: return cnt, lst[:-1]

def make_rounds():
    rounds = []
    for r in range(N):
        round = []
        for c in range(N):
            round.append((r, c))
        rounds.append(round)
    for c in range(N):
        round = []
        for r in range(N-1, -1, -1):
            round.append((r, c))
        rounds.append(round)
    for r in range(N-1, -1, -1):
        round = []
        for c in range(N-1, -1, -1):
            round.append((r, c))
        rounds.append(round)
    for c in range(N-1, -1, -1):
        round = []
        for r in range(N):
            round.append((r, c))
        rounds.append(round)
    return rounds

def get_score(k):
    for r, c in rounds[k%(4*N)]:
        for i, group in enumerate(groups):
            if (r, c) in group[:cnts[i]]:
                idx = group.index((r, c))
                groups[i] = group[:cnts[i]][::-1] + group[cnts[i]:][::-1]
                return (idx+1)**2
    return 0

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
rounds = make_rounds()

V = [[0]*N for _ in range(N)]
groups = []
cnts = []
idx = 1
for r in range(N):
    for c in range(N):
        if A[r][c] == 1:
            cnt, group = dfs(r, c, idx)
            groups.append(group)
            cnts.append(cnt)
            idx += 1

answer = 0
for k in range(K):
    for i, group in enumerate(groups):
        groups[i] = [group[-1]] + group[:-1]
    answer += get_score(k)
print(answer)