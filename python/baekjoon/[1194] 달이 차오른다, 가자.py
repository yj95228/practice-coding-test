import sys
from collections import deque
input = sys.stdin.readline

def find():
    for r in range(1, N+1):
        for c in range(1, M+1):
            if A[r][c] == '0':
                A[r][c] = '.'
                return r, c

def solve():
    global V
    queue = deque([(0, 1, sr, sc)])
    while queue:
        turn, key, r, c = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = r+dx, c+dy
            if V[nx][ny] & key == key: continue
            if A[nx][ny] == '1': return turn+1
            elif A[nx][ny] == '.':
                V[nx][ny] = key
                queue.append((turn+1, key, nx, ny))
            elif A[nx][ny].isupper():
                if key & 1 << ord(A[nx][ny])-ord('A')+1:
                    V[nx][ny] = key
                    queue.append((turn+1, key, nx, ny))
            elif A[nx][ny].islower():
                if key & 1 << ord(A[nx][ny])-ord('a')+1:
                    V[nx][ny] = key
                    queue.append((turn+1, key, nx, ny))
                else:
                    num = ord(A[nx][ny])-ord('a')+1
                    new_key = key + (1 << num)
                    V[nx][ny] = new_key
                    queue.append((turn+1, new_key, nx, ny))
    return -1

N, M = map(int, input().split())
A = [['#']*(M+2)] + [['#'] + list(input().rstrip()) + ['#'] for _ in range(N)] + [['#']*(M+2)]
V = [[0]*(M+2) for _ in range(N+2)]
sr, sc = find()
V[sr][sc] = 1
print(solve())