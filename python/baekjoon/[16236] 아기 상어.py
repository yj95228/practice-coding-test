# TODO: 구현이 어려웠음 / 물고기 위치 딕셔너리 저장해서 풀어보기
# 1차 시도 (64분): 116656kb 180ms
# 2차 시도 (70분): 1차 시도에서 범위 체크 안하려고 패딩했었는데 패딩 안 하면 시간 동일 (180ms -> 180ms)
# 3차 시도 (87분): 같은 거리들을 정렬하는 방식이 아닌 최소값 저장하는 방식 (180ms -> 164ms)
# https://www.acmicpc.net/problem/16926
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def bfs(x,y):
    global nr, nc, answer, eat, size
    queue = deque([(x,y,0)])
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    mr,mc = N,N

    while queue:
        # 같은 거리만큼 bfs 돌기
        for _ in range(len(queue)):
            r, c, d = queue.popleft()
            if 0 < matrix[r][c] < size:
                if r < mr:
                    mr,mc = r,c
                elif r == mr:
                    if c < mc:
                        mr,mc = r,c
            for (dx, dy) in ((-1,0),(0,-1),(0,1),(1,0)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] <= size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,d+1))

        if (mr,mc) != (N,N):
            nr,nc = mr,mc
            matrix[nr][nc] = 0
            eat += 1
            answer += d
            if eat == size:
                size += 1
                eat = 0
            return True

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
size,nr,nc = 2,0,0  # 상어 현재 크기, 위치
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 9:
            nr, nc = r, c
            matrix[r][c] = 0

# 시간, 먹은 물고기 수, 먹는중
answer, eat, ing = 0, 0, True
while ing:
    ing = bfs(nr,nc)
print(answer)