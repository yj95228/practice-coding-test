# https://www.acmicpc.net/problem/5427
'''
1차 제출: 백두산 때 풀었는데 왜 잘 모르겠지
2차 제출: 상근이 있는 곳에 빈 공간 처리해놓고 불 있던 공간에 빈 공간 처리 안함
3차 제출: 불과 상근이가 동시에 도착하는 경우를 고려하지 않음.. ㅠㅠ
4차 제출: 동시 도착 시간을 봐야되는데 안 봄... 정신차려
5차 제출: 부등호로 바꿔서 제출해보고 안되면 불을 큐에 먼저 넣어봐ㅑ겟다
6차 제출: 239116kb 936ms
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        where, r, c = queue.popleft()
        
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if where == FIRE:
                if 0 <= nx < H and 0 <= ny < W and \
                not fire[nx][ny] and matrix[nx][ny] == EMPTY:
                    fire[nx][ny] = fire[r][c] + 1
                    queue.append((FIRE, nx, ny))
            elif where == HERE:
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited[nx][ny] and not fire[nx][ny] and matrix[nx][ny] == EMPTY:
                        visited[nx][ny] = visited[r][c] + 1
                        queue.append((HERE, nx, ny))
                else:
                    return visited[r][c]
                
    return 'IMPOSSIBLE'

T = int(input())
EMPTY, WALL, HERE, FIRE = '.', '#', '@', '*'
for tc in range(1,T+1):
    W, H = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(H)]

    queue = deque()
    visited = [[0]*W for _ in range(H)]
    fire = [[0]*W for _ in range(H)]
    fire_list = []
    
    sr, sc = None, None
    for r in range(H):
        for c in range(W):
            if matrix[r][c] == HERE:
                sr, sc = r, c
                visited[r][c] = 1
                matrix[r][c] = EMPTY
            elif matrix[r][c] == FIRE:
                queue.append((FIRE, r,c))
                fire[r][c] = 1
                matrix[r][c] = EMPTY

    queue.append((HERE, sr, sc))

    print(bfs())