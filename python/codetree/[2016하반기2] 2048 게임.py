import sys
input = sys.stdin.readline

def rotate(A, d):
    B = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if d == 1:
                B[r][c] = A[N-c-1][r]
            elif d == 2:
                B[r][c] = A[N-r-1][N-c-1]
            else:
                B[r][c] = A[c][N-r-1]
    return B

def play(A):
    B = []
    for r in range(N):
        stack = []
        two = False
        for c in range(N):
            if A[r][c] == 0: continue
            if two:
                two = False
                stack.append(A[r][c])
            else:
                if stack and stack[-1] == A[r][c]:
                    two = True
                    stack.append(stack.pop()*2)
                else:
                    stack.append(A[r][c])
        B.append(stack+[0]*(N-len(stack)))
    return B

def recur(n, A):
    global answer
    if n == 5:
        for r in range(N):
            for c in range(N):
                answer = max(answer, A[r][c])
        return
    recur(n+1, play(A))
    recur(n+1, play(rotate(A, 1)))
    recur(n+1, play(rotate(A, 2)))
    recur(n+1, play(rotate(A, 3)))

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 0
recur(0, A)
print(answer)