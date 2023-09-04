# https://www.acmicpc.net/problem/1189
# FIXME: 처음 방문 체크 까먹었었음
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(r,c,k):
    global answer
    if (r,c) == (1,C) and k == K:
        answer += 1
        return
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = r+dx, c+dy
        if not visited[nx][ny] and matrix[nx][ny] != 'T':
            visited[nx][ny] = True
            dfs(nx,ny,k+1)
            visited[nx][ny] = False

R, C, K = map(int, input().split())
matrix = [['T']*(C+2)] + [['T'] + list(input().rstrip()) + ['T'] for _ in range(R)] + [['T']*(C+2)]
visited = [[False]*(C+2) for _ in range(R+2)]
visited[R][1] = True    # 실수한 부분
answer = 0
dfs(R,1,1)
print(answer)