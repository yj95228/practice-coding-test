'''
0. 코드 구상하면서
- 블록 그룹 일반 블록 색이 다 같아야 한다는걸 읽고 적기까지 해놓고 구현할 때 되니 빼먹음
- 중력 규칙을 파악하는 데 어려웠는데 검은색 블록은 중력 작용되지 않는다는 것이 왜 안 적혀있지 했는데 문제에 적혀있는데 내가 못 본거구나.....

1차. 구현 시간 70분 (실패)
- 문제가 어렵지는 않았는데 구현 시간이 많이 늦어진 것 같다
- 시키는 대로 구현하면 되니까 엣지케이스가 있을지 모르겠지만 일단 TC 다 맞으니까 제출
- 2048에서 시계 반시계 돌리고 나니까 배열 돌리는건 어렵지 않았음

2차. 내가 뭘 놓쳤을까
- 반시계는 문제 없는거 확인함 [v]
- 중력도 문제 없는것 같음 [v]
- 혹시 max key값 달아야하나..?? key값 안 달아도 tuple 내 값으로 max 된다고 했는데 일단 넣으면 통과하는지 제출해봐야겠다...

3차. 무지개 블록이 블록 그룹 여러 개에 속할 수 있다는 사실을 몰랐음 ㅠㅠ

4차. (20:18, 117020kb, 224ms) 무지개 블록을 셀 때 stack 들어갈 때마다 +1 해줬어야 했는데 stack의 인자로 넘기다 보니 의도대로 증가되지 않았음 (from 성진님)

5차. (20:21, 117012kb, 232ms) lst로 이미 그룹의 수를 세고 있으므로 따로 group으로 변수를 둬서 셀 필요가 없음
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(x,y):
    stack = [(x,y)]
    groups[x][y] = True
    color = matrix[x][y]
    block, rainbow = 1, 0
    rainbow_list = []

    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if not groups[nx][ny] and (matrix[nx][ny] == color or matrix[nx][ny] == 0):
                groups[nx][ny] = True
                block += 1
                if matrix[nx][ny] == 0:
                    rainbow += 1
                    rainbow_list.append((nx,ny))
                stack.append((nx, ny))

    for r, c in rainbow_list:
        groups[r][c] = 0


    if block >= 2:
        lst.append((block, rainbow, x, y))
        return True
    return False

def down():
    for c in range(1,N+1):
        for r in range(N,0,-1):
            if matrix[r][c] is not None: continue
            now = r
            while matrix[now][c] is None:
                now -= 1
            if matrix[now][c] != -1:
                matrix[r][c], matrix[now][c] = matrix[now][c], matrix[r][c]

N, M = map(int, input().split())
matrix = [[-1]*(N+2)] +\
         [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] +\
         [[-1]*(N+2)]
answer = 0

while True:
    groups = [[0]*(N+2) for _ in range(N+2)]
    lst = []

    # 1. 그룹 만들기
    for r in range(1,N+1):
        for c in range(1,N+1):
            if matrix[r][c] is not None and matrix[r][c] > 0 and not groups[r][c]:
                dfs(r,c)

    if not lst:
        print(answer)
        break

    # 2. 가장 큰 블록 그룹 찾아서 모든 블록 제거
    B, _, x, y = max(lst, key=lambda x: (x[0], x[1], x[2], x[3]))
    visited = [[False]*(N+2) for _ in range(N+2)]
    stack = [(x,y)]
    visited[x][y] = True
    color = matrix[x][y]
    matrix[x][y] = None
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if not visited[nx][ny] and (matrix[nx][ny] == color or matrix[nx][ny] == 0):
                visited[nx][ny] = True
                matrix[nx][ny] = None
                stack.append((nx, ny))

    # 블록의 수 제곱만큼 점수 획득
    answer += B*B

    # 중력 작용
    down()

    # 90도 반시계 방향 회전
    matrix = list(map(list,zip(*matrix)))[::-1]

    # 중력 작용
    down()