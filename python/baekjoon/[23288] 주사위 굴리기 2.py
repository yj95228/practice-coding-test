'''
- 온풍기 문제 벽이 칸으로 되어있는게 아니고 선으로 되어있다는 사실을 알기 전에는
  온풍기가 더 쉬울 줄 알고 5분 정도 코드 짜보다가 주사위 굴리러 옴
- 시계, 반시계, 반대 방향에서 방향만 돌리면 되는데 주사위도 같이 돌림
- 위치 옮기고 나서 다음 반복문 돌때 옮긴 위치에서 시작하게 바꾸는거 까먹지 말기 
'''
# https://www.acmicpc.net/problem/23288
import sys
input = sys.stdin.readline

def dfs(x,y):
    result = 1
    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True
    stack = [(x,y)]
    while stack:
        r, c, = stack.pop()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M and\
            not visited[nx][ny] and matrix[nx][ny] == matrix[r][c]:
                visited[nx][ny] = True
                result += 1
                stack.append((nx,ny))
    return result

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dice = [1,2,3,4,5,6]                # 위(0), 뒤(1), 동(2), 서(3), 앞(4), 밑(5)
dt = ((0,1),(1,0),(0,-1),(-1,0))    # -> 시계방향 <- 반시계방향
r, c, d = 0, 0, 0                   # 현재 위치, 현재 방향
answer = 0
dice_rotate = [
    [3,1,0,5,4,2],  #동
    [1,5,2,3,0,4],  #남
    [2,1,5,0,4,3],  #서
    [4,0,2,3,5,1],  #북
]
for _ in range(K):
    dx, dy = dt[d]

    if not (0 <= r+dx < N and 0 <= c+dy < M):
        d = (d+2)%4
    dx, dy = dt[d]
    dice = list(map(lambda x: dice[x], dice_rotate[d]))
    nx, ny = r+dx, c+dy
    answer += dfs(nx, ny)*matrix[nx][ny]
    r, c = nx, ny

    if dice[-1] > matrix[nx][ny]:
        d = (d+1)%4
    elif dice[-1] < matrix[nx][ny]:
        d = (d-1)%4

print(answer)