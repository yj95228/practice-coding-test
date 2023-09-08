# https://www.acmicpc.net/problem/1726
import sys
import heapq
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(input().split()) for _ in range(M)]
sr, sc, sd = map(lambda x: int(x)-1, input().split())
er, ec, ed = map(lambda x: int(x)-1, input().split())
INF = 987654321
visited = [[[INF]*4 for _ in range(N)] for _ in range(M)]
visited[sr][sc][sd] = 0
queue = []
heapq.heappush(queue, (0, sr, sc, sd))
while queue:
    cnt, r, c, d = heapq.heappop(queue)
    if (r,c,d) == (er,ec,ed):
        print(cnt)
        break
    else:
        if visited[r][c][d] < cnt: continue
        dx, dy = [0,0,1,-1][d], [1,-1,0,0][d]
        if 0 <= r+dx < M and 0 <= c+dy < N and matrix[r+dx][c+dy] == '0':
            if 0 <= r+2*dx < M and 0 <= c+2*dy < N and matrix[r+2*dx][c+2*dy] == '0':
                if 0 <= r+3*dx < M and 0 <= c+3*dy < N and matrix[r+3*dx][c+3*dy] == '0':
                    if cnt+1 < visited[r+3*dx][c+3*dy][d]:
                        visited[r+3*dx][c+3*dy][d] = cnt+1
                        heapq.heappush(queue, (cnt+1, r+3*dx, c+3*dy, d))
                if cnt+1 < visited[r+2*dx][c+2*dy][d]:
                    visited[r+2*dx][c+2*dy][d] = cnt+1
                    heapq.heappush(queue, (cnt+1, r+2*dx, c+2*dy, d))
            if cnt+1 < visited[r+dx][c+dy][d]:
                visited[r+dx][c+dy][d] = cnt+1
                heapq.heappush(queue, (cnt+1, r+dx, c+dy, d))
        if d < 2:
            for x in [2,3]:
                if cnt+1 < visited[r][c][x]:
                    visited[r][c][x] = cnt+1
                    heapq.heappush(queue, (cnt+1, r, c, x))
        else:
            for x in [0,1]:
                if cnt+1 < visited[r][c][x]:
                    visited[r][c][x] = cnt+1
                    heapq.heappush(queue, (cnt+1, r, c, x))

# 강사님 코드
import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().rstrip().split())
fac_map = [input().split() for _ in range(M)]
sr,sc,sdir = map(lambda a: int(a)-1,input().split())
tr,tc,tdir = map(lambda a: int(a)-1,input().split())
dr = (0,0,1,-1) # 동(우) 서(좌) 남(하) 북(상)
dc = (1,-1,0,0)
def solve():
    print(bfs())

def bfs():
    que = deque()
    visited = [[[-1]*N for _ in range(M)] for _ in range(4)]  # 매위치마다 방향기준으로 방문관리 : 3차원

    visited[sdir][sr][sc]=0
    que.append((sr,sc,sdir))

    while que:
        r,c,dir = que.popleft()
        if r==tr and c==tc and dir==tdir: return visited[tdir][r][c]

        # 1-3칸 이동
        for m in range(1,4):
            nr = r + m*dr[dir]
            nc = c + m*dc[dir]
            if nr<0 or nr>=M or nc<0 or nc>=N or fac_map[nr][nc]=='1': break # 경계를 벗어나거나 궤도가 없으면
            if visited[dir][nr][nc]>-1: continue # 현방향으로 해당 위치에 방문한 적이 있었으면

            visited[dir][nr][nc] = visited[dir][r][c]+1
            que.append((nr,nc,dir))
        # 좌,우 회전 : 동/서 - 우:+2, 좌:두방향의합3,    남/북 - 좌:+2, 우: 두방향의합3
        rdir = ((dir+2)%4, 3-dir)
        for nd in rdir:
            if visited[nd][r][c]>-1: continue
            visited[nd][r][c] = visited[dir][r][c]+1
            que.append((r,c,nd))

    return -1
solve()