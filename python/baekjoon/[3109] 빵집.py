import sys
input = sys.stdin.readline

# 재귀
def recur(rr, r, c):
    global answer
    if c == M:
        answer += 1
        return True
    for d in [-1,0,1]:
        nr = r+d
        if 0 <= nr < N and not V[nr][c] and A[nr][c] == '.':
            V[nr][c] = rr+1
            if recur(rr, nr, c+1):
                return True

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[0]*M for _ in range(N)]
answer = 0
for x in range(N):
    recur(x, x, 1)
print(answer)

# 스택
N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[0]*M for _ in range(N)]
answer = 0
for x in range(N):
    stack = [(x, 0)]
    while stack:
        r, c = stack.pop()
        if V[r][c]: continue
        if c == M-1:
            answer += 1
            break
        V[r][c] = 1
        for d in [1,0,-1]:
            nr = r+d
            if 0 <= nr < N and not V[nr][c+1] and A[nr][c+1] == '.':
                stack.append((nr, c+1))
print(answer)

# flag로 재귀 빨리 return시키기
def recur(rr, r, c):
    global answer, flag
    if flag: return
    if c == M-1:
        answer += 1
        flag = True
        return
    V[r][c] = rr+1
    for d in [-1,0,1]:
        nr = r+d
        if 0 <= nr < N and not V[nr][c+1] and A[nr][c+1] == '.':
            recur(rr, nr, c+1)

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
V = [[0]*M for _ in range(N)]
answer = 0
for x in range(N):
    flag = False
    recur(x, x, 0)
print(answer)