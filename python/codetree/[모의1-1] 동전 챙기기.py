# https://www.codetree.ai/training-field/home/timer/problems/collect-coins/description
from sys import stdin
from collections import deque
input = stdin.readline

def bfs(arr):
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1
    queue = deque([(sr, sc, 0, 0)])
    mx = 0
    while queue:
        r, c, coin, cnt = queue.popleft()
        if coin < mx: continue
        if coin == 3 and A[r][c] == 'E':
            return cnt
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and A[nx][ny] != '#':
                if A[nx][ny].isdigit() and int(A[nx][ny]) == arr[coin]:
                    visited = [[0]*N for _ in range(N)]
                    visited[nx][ny] = 1
                    queue.append((nx, ny, coin+1, cnt+1))
                    mx = coin+1
                    break
                else:
                    queue.append((nx, ny, coin, cnt+1))
                    visited[nx][ny] = 1
    return 987654321

def recur(n, start, arr):
    global answer
    if len(arr) == 3:
        answer = min(answer, bfs(arr+['E']))
        return
    for i in range(start, length):
        recur(n+1, i+1, arr+[coins[i]])

N = int(input())
A = [list(input().rstrip()) for _ in range(N)]
sr, sc, coins = None, None, set()
for r in range(N):
    for c in range(N):
        if A[r][c] == 'S':
            sr, sc = r, c
        elif A[r][c].isdigit():
            coins.add(int(A[r][c]))
coins = sorted(list(coins))
length = len(coins)
answer = 987654321
recur(0, 0, [])
print(-1 if answer == 987654321 else answer)