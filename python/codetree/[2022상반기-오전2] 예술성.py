# 1차 제출: (풀이시간 75분) 152ms, 31MB
# - 십자가 시계방향 돌리는거 실수가 있었음
# https://www.codetree.ai/training-field/frequent-problems/problems/artistry/description?page=3&pageSize=20
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def get_score():
    # 그룹 정하기
    groups = [[0]*(N+2) for _ in range(N+2)]    # 그룹 좌표에 저장
    group = 1                                   # 그룹명
    large = [0]                                 # 칸
    num = [0]                                   # 수
    groups_rc = [[]]                            # 그룹 좌표

    for r in range(1,N+1):
        for c in range(1,N+1):
            if groups[r][c]: continue
            stack = [(r,c)]
            groups[r][c] = group
            length = 1
            result = [(r,c)]
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if matrix[nx][ny] == 11: continue
                    if matrix[nx][ny] == matrix[r][c] and not groups[nx][ny]:
                        groups[nx][ny] = group
                        length += 1
                        stack.append((nx,ny))
                        result.append((nx,ny))
            group += 1
            large.append(length)
            num.append(matrix[r][c])
            groups_rc.append(result)

    # 그룹 간의 예술점수 정하기 -> 초기 예술 점수
    art_score = 0
    for i in range(1,group-1):
        for j in range(i+1,group):
            together = 0
            for r, c in groups_rc[i]:
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+dx, c+dy
                    if groups[nx][ny] == j:
                        together += 1
            art_score += (large[i]+large[j])*num[i]*num[j]*together
    return art_score

def rotate():
    # 그림에 대한 1회전, 2회점, 3회전 예술 점수 합 각각 구하기
    new_matrix = [row[:] for row in matrix]
    half = N//2+1

    # 십자가
    for r in range(1,half):
        new_matrix[half][r] = matrix[r][half]
    for c in range(1,half):
        new_matrix[N-c+1][half] = matrix[half][c]
    for r in range(N,half,-1):
        new_matrix[half][r] = matrix[r][half]
    for c in range(N,half,-1):
        new_matrix[N-c+1][half] = matrix[half][c]

    # 정사각형
    for i in range(1,N,half):
        for j in range(1,N,half):
            for r in range(N//2):
                for c in range(N//2):
                    new_matrix[i+r][j+c] = matrix[i+N//2-c-1][j+r]
    return new_matrix

N = int(input())
matrix = [[11]*(N+2)] + [[11] + list(map(int, input().split())) + [11] for _ in range(N)] + [[11]*(N+2)]

# 초기 예술 점수
answer = get_score()

# 1회전 이후 예술 점수
matrix = rotate()
answer += get_score()

# 2회전 이후 예술 점수
matrix = rotate()
answer += get_score()

# 3회전 이후 예술 점수
matrix = rotate()
answer += get_score()

print(answer)

# 2차 풀이
'''
- 1차. 10:20 ~ 10:56 전에는 맞닿아 있는 변은 생각보다 쉽게 구하고 회전이 어려웠는데 이번에는 반대임..
'''

def dfs(x,y,group):
    groups[x][y] = group
    stack = [(x,y)]
    color = matrix[x][y]
    cnt = 1
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not groups[nx][ny] and matrix[nx][ny] == color:
                cnt += 1
                groups[nx][ny] = group
                stack.append((nx,ny))
    cnts.append(cnt)

def johwa(x,y):
    color = groups[x][y]
    v_groups[color] = True
    stack = [(x,y)]
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if groups[nx][ny] == color:
                    stack.append((nx,ny))
                    visited[nx][ny] = True
                else:
                    score[color][groups[nx][ny]] += 1

def rotate(arr):
    narr = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if r == N//2 or c == N//2:
                narr[r][c] = arr[c][N-r-1]
    for r in range(0,N,N//2+1):
        for c in range(0,N,N//2+1):
            for i in range(N//2):
                for j in range(N//2):
                    narr[r+i][c+j] = arr[r+N//2-j-1][c+i]
    return narr

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for turn in range(4):
    group = 1
    groups = [[0]*N for _ in range(N)]
    nums, cnts = [0], [0]
    for r in range(N):
        for c in range(N):
            if not groups[r][c]:
                dfs(r,c,group)
                nums.append(matrix[r][c])
                group += 1

    v_groups = [0]*group
    score = [[0]*group for _ in range(group)]
    for r in range(N):
        for c in range(N):
            if not v_groups[groups[r][c]]:
                johwa(r,c)

    for i in range(1,group-1):
        for j in range(i+1,group):
            answer += (cnts[i]+cnts[j])*nums[i]*nums[j]*score[i][j]

    if turn == 3: break
    matrix = rotate(matrix)

print(answer)


# 3차 풀이
def dfs(x, y, idx):
    G[x][y] = idx
    stack = [(x, y)]
    num = A[x][y]
    cnt = 1
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not G[nx][ny] and A[nx][ny] == num:
                G[nx][ny] = idx
                stack.append((nx, ny))
                cnt += 1
    return cnt, num, x, y

def find(x, y, num, g):
    V = [[0]*N for _ in range(N)]
    stack = [(x, y)]
    V[x][y] = 1
    cnt = 0
    while stack:
        r, c = stack.pop()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = r + dx, c + dy
            if 0 <= nx < N and 0 <= ny < N and not V[nx][ny]:
                if G[nx][ny] == num:
                    V[nx][ny] = 1
                    stack.append((nx, ny))
                elif G[nx][ny] == g:
                    cnt += 1
    return cnt

N = int(input())
turn = dict()
for r in range(N):
    for c in range(N):
        if r == N//2 or c == N//2:
            turn[(r, c)] = (N-c-1, r)

def rotate(A):
    B = [row[:] for row in A]
    for (r, c), (nx, ny) in turn.items():
        B[nx][ny] = A[r][c]
    for r in range(N // 2):
        for c in range(N // 2):
            B[c][N // 2 - r - 1] = A[r][c]
            B[N // 2 + 1 + c][N // 2 - r - 1] = A[N // 2 + 1 + r][c]
            B[c][N - r - 1] = A[r][N // 2 + 1 + c]
            B[N // 2 + 1 + c][N - r - 1] = A[N // 2 + 1 + r][N // 2 + 1 + c]
    return B

A = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for time in range(4):
    G = [[0]*N for _ in range(N)]
    group = []
    idx = 1
    for r in range(N):
        for c in range(N):
            if not G[r][c]:
                group.append(dfs(r, c, idx))
                idx += 1

    for i in range(idx-2):
        cnt1, num1, r1, c1 = group[i]
        for j in range(i+1, idx-1):
            cnt2, num2, r2, c2 = group[j]
            if cnt1 > num1:
                answer += (cnt1+cnt2)*num1*num2*find(r1, c1, i+1, j+1)
            else:
                answer += (cnt1+cnt2)*num1*num2*find(r2, c2, j+1, i+1)

    if time == 3: break
    A = rotate(A)
print(answer)