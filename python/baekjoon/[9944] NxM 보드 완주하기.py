import sys
input = sys.stdin.readline

def recur(n, r, c, cnt):
    global answer
    if cnt == 0:
        answer = min(answer, n)
        return
    elif n > answer: return
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        s = 1
        while True:
            nx, ny = r+s*dx, c+s*dy
            if A[nx][ny] == '*': break
            s += 1
        if s == 1: continue
        for k in range(1, s):
            A[r+k*dx][c+k*dy] = '*'
        recur(n+1, r+(s-1)*dx, c+(s-1)*dy, cnt-s+1)
        for k in range(1, s):
            A[r+k*dx][c+k*dy] = '.'

turn = 0
while True:
    try:
        N, M = map(int, input().split())
        A = [['*']*(M+2)] + [['*'] + list(input().rstrip()) + ['*'] for _ in range(N)] + [['*']*(M+2)]
        turn += 1
        answer = 987654321
        blank = [(r, c) for r in range(1, N+1) for c in range(1, M+1) if A[r][c] == '.']
        length = len(blank)
        for r, c in blank:
            A[r][c] = '*'
            recur(0, r, c, length-1)
            A[r][c] = '.'
        print(f'Case {turn}: {-1 if answer == 987654321 else answer}')
    except: break