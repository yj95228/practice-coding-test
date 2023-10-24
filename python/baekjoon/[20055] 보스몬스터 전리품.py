# https://www.acmicpc.net/problem/20005
from sys import stdin
input = stdin.readline

def bfs(x, y):
    V = [[0]*N for _ in range(M)]
    V[x][y] = 1
    queue = [(x, y)]
    time = 0
    while queue:
        temp_q = []
        for r, c in queue:
            if A[r][c] == 'B':
                players[A[x][y]][1] = time
                return
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < M and 0 <= ny < N and not V[nx][ny] and A[nx][ny] != 'X':
                    V[nx][ny] = 1
                    temp_q.append((nx, ny))
        time += 1
        queue = temp_q

M, N, P = map(int, input().split())
A = [list(input().rstrip()) for _ in range(M)]
players = dict()
for _ in range(P):
    id, dps = input().split()
    players[id] = [int(dps), -1, False]
boss = int(input())
for r in range(M):
    for c in range(N):
        if A[r][c].islower():
            bfs(r, c)
time = min([player[1] for player in players.values() if player[1] != -1])
while True:
    damage = 0
    for p, player in players.items():
        if player[1] == -1: continue
        if player[1] <= time:
            damage += player[0]
            players[p][2] = True
    boss -= damage
    if boss <= 0: break
    time += 1
print(sum([player[2] for player in players.values()]))