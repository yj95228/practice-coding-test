from sys import stdin
stdin = open('input.txt','r')
input = stdin.readline

def solve(arr):
    for r, c in teacher:
        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            s = 1
            while True:
                nx, ny = r+s*dx, c+s*dy
                if A[nx][ny] == 'S':
                    return False
                elif (nx, ny) in arr or A[nx][ny] == 'O':
                    break
                else: s += 1
    return True

def recur(n, start, arr):
    global answer
    if answer == 'YES': return
    if n == 3:
        if solve(arr):
            answer = 'YES'
        return
    for x in range(start, length):
        recur(n+1, x+1, arr+[can[x]])

N = int(input())
A = [['O']*(N+2)] + [['O'] + list(input().split()) + ['O'] for _ in range(N)] + [['O']*(N+2)]
teacher, can = [], []
for r in range(1, N+1):
    for c in range(1, N+1):
        if A[r][c] == 'T':
            teacher.append((r, c))
        elif A[r][c] == 'X':
            can.append((r, c))
length = len(can)
answer = 'NO'
recur(0, 0, [])
print(answer)