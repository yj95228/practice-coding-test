import sys
input = sys.stdin.readline

def play(arr):
    for rr, cc in arr:
        A[rr][cc] = 1

    success = True
    for c in range(N):
        if not success: break
        now = c
        for r in range(H):
            if A[r][now]: now += 1
            elif 0 <= now-1 and A[r][now-1]: now -= 1
        if now == c: continue
        else:
            success = False
            break

    for rr, cc in arr:
        A[rr][cc] = 0
    return success

def recur(n, start, arr):
    global answer
    if play(arr):
        answer = min(answer, n)
        return
    elif n == 3 or n >= answer: return
    for x in range(start, length):
        if V[x]: continue
        rr, cc = can[x]
        for r, c in arr:
            if (rr, cc) == (r, c+1) or (rr, cc) == (r, c-1): break
        else:
            V[x] = 1
            recur(n+1, x+1, arr+[(rr, cc)])
            V[x] = 0

N, M, H = map(int, input().split())
A = [[0]*N for _ in range(H)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    A[a][b] = 1

can = []
for r in range(H):
    for c in range(N-1):
        if not A[r][c]:
            if 0 <= c-1 and A[r][c-1]: continue
            if c+1 < N and A[r][c+1]: continue
            can.append((r, c))

length = len(can)
V = [0]*length
answer = 4
recur(0, 0, [])
print(-1 if answer == 4 else answer)