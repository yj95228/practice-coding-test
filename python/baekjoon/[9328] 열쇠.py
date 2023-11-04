import sys
from collections import deque
input = sys.stdin.readline

def init():
    global V, answer, queue
    V = [[0] * (M + 2) for _ in range(N + 2)]
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if r == 1 or c == 1 or r == N or c == M:
                if A[r][c] == '*': continue
                elif A[r][c] == '.': pass
                elif A[r][c] == '$': answer += 1
                elif A[r][c].isupper():
                    if alpha[ord(A[r][c]) - ord('A')]: pass
                    else: continue
                elif A[r][c].islower():
                    alpha[ord(A[r][c]) - ord('a')] = 1
                start.add((r, c))
                V[r][c] = 1
                A[r][c] = '.'
    queue = deque(start)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [['*']*(M+2)] + [['*'] + list(input().rstrip()) + ['*'] for _ in range(N)] + [['*']*(M+2)]
    keys = list(input().rstrip())
    alpha = [0]*26
    for x in keys:
        if x == '0': break
        alpha[ord(x)-ord('a')] = 1

    answer = 0
    V = [[0] * (M + 2) for _ in range(N + 2)]
    start = set()
    queue = None
    init()
    while queue:
        rr, cc = queue.popleft()
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = rr+dx, cc+dy
            if V[nx][ny]: continue
            elif A[nx][ny] == '*': continue
            elif A[nx][ny] == '.': pass
            elif A[nx][ny] == '$':
                answer += 1
                init()
            elif A[nx][ny].isupper():
                if alpha[ord(A[nx][ny]) - ord('A')]: pass
                else: continue
            elif A[nx][ny].islower():
                alpha[ord(A[nx][ny]) - ord('a')] = 1
                init()
            V[nx][ny] = 1
            queue.append((nx, ny))
            A[nx][ny] = '.'
    print(answer)