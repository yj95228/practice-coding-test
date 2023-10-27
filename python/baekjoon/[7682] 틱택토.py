from sys import stdin
stdin = open('input.txt','r')
input = stdin.readline

def check(A):
    if A[0][0] == A[1][1] == A[2][2] != '.': return True
    if A[0][2] == A[1][1] == A[2][0] != '.': return True
    for x in range(3):
        if A[x][0] == A[x][1] == A[x][2] != '.':
            return True
        if A[0][x] == A[1][x] == A[2][x] != '.':
            return True

def recur(n, A):
    if check(A) or n == 9:
        ttt.add(''.join(map(lambda x: ''.join(x), A)))
        return
    for i in range(9):
        if visited[i]: continue
        visited[i] = 1
        r, c = can[i]
        A[r][c] = 'O' if n%2 else 'X'
        recur(n+1, [row[:] for row in A])
        A[r][c] = '.'
        visited[i] = 0

A = [['.']*3 for _ in range(3)]
can = [(r,c) for r in range(3) for c in range(3)]
visited = [0]*9
ttt = set()
recur(0, [['.']*3 for _ in range(3)])

while True:
    txt = input().rstrip()
    if txt == 'end': break
    else: print('valid' if txt in ttt else 'invalid')