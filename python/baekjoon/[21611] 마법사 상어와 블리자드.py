'''
- 구슬 이동 while문 헷갈려서 꽤 걸림 -> while True 쓰고 break하자
- 파괴랑 폭발이랑 용어가 헷갈려서 둘다 세는줄 알았네
- 마지막 달팽이 부분 인덱스 처리 애매해서 그냥 (0,0) 넣고 처리했는데 TC 나오는대로 잘 구현되길래 일단 ㄱ
- 1차. 10:53 또 실수 나올까봐 걱정인데 일단 TC 맞고 예제대로 잘 동작하니 제출해보자... (시간초과)
- 2차. 11:10 while문 어딘가에서 break가 안되는것 같아
    - i는 커지면 break 되게 조건 하나 추가해보자
    - i+1 >= N*N-1 말고 i >= N*N-1라고 바꿈
    - 나는 for문이 더 좋은데 for문으로 어떻게 짜야될지 감이 안 잡혀서 시간되면 for문으로 바꿔짜자
- 3차. 폭발할 때는 이미 이동한 후니까 색깔 다르면 continue말고 break해보자
- 4차. 3차는 원상복귀시키고 폭발 안되면 break 먼저 시키고 이동하기
- 5차. 코드 갈아엎고 달팽이 배열을 일자로 펴서 풀었음
- 6차. 마지막 달팽이 넣었던거 다시 빼고 제출
- 7차. 스택 연산 다 하고 나서 마지막 스택에 남은 4개 연속 구슬들 처리 (116616kb, 208ms)
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dt = ((-1,0),(1,0),(0,-1),(0,1))
score = [0,0,0]
sr, sc = N//2, N//2

# 달팽이 미리 만들기
snail = []
snail_dt = ((0,-1),(1,0),(0,1),(-1,0))
visited = [[False]*N for _ in range(N)]
r, c, d = N//2, N//2, 0
visited[r][c] = True

for _ in range(N*N-1):
    dx, dy = snail_dt[d]
    nx, ny = r+dx, c+dy
    snail.append((nx,ny))
    visited[nx][ny] = True
    dx, dy = snail_dt[(d+1)%4]
    nnx, nny = nx+dx, ny+dy
    if not visited[nnx][nny]:
        d = (d+1)%4
    r, c = nx, ny

for _ in range(M):
    D, S = map(int, input().split())

    # 1. 방향 d와 거리 s만큼 구슬 파괴
    dx, dy = dt[D-1]
    for i in range(1,S+1):
        nx, ny = sr+i*dx, sc+i*dy
        if not (0 <= nx < N and 0 <= ny < N): continue
        matrix[nx][ny] = 0

    # 2. 빈칸에 구슬 이동
    lst = []
    for r, c in snail:
        if matrix[r][c]:
            lst.append(matrix[r][c])

    # 3. 구슬 폭발 (4개 이상 연속하는 구슬이 있을 때, 더이상 폭발할 수 없을때까지)
    while True:
        cnt, stack, explode = 1, [], False
        for x in lst:
            if stack:
                if stack[-1] == x:
                    cnt += 1
                else:
                    if cnt >= 4:
                        explode = True
                        for _ in range(cnt):
                            score[stack.pop()-1] += 1
                    cnt = 1
            else:
                cnt = 1
            stack.append(x)
        if cnt >= 4:
            for _ in range(cnt):
                score[stack.pop()-1] += 1
        lst = stack
        if not explode: break

    # 4. 구슬 변화화
    new_list = []
    for i in range(len(lst)):
        x = lst[i]
        if i == 0 or new_list[-1] != x:
            new_list.append(1)
            new_list.append(x)
        else:
            new_list[-2] += 1

    new_matrix = [[0]*N for _ in range(N)]
    for i in range(len(new_list)):
        if i >= N*N-1: break
        r, c = snail[i]
        new_matrix[r][c] = new_list[i]

    matrix = new_matrix

print(score[0]+2*score[1]+3*score[2])