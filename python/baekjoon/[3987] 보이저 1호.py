import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
PR, PC = map(int, input().split())
r, c, answer, send = PR-1, PC-1, 0, None
direction = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
backslash = {'U':'L','L':'U','R':'D','D':'R'}
slash = {'R':'U','L':'D','D':'L','U':'R'}
queue = []
for d in list('URDL'):
    if matrix[r][c] == '\\': queue.append((r,c,d,backslash[d],1))
    elif matrix[r][c] == '/': queue.append((r,c,d,slash[d],1))
    elif matrix[r][c] == '.': queue.append((r,c,d,d,1))
while queue:
    current = queue.pop(0)
    r,c,start,d,result = current
    if result > 1 and start == d and (r,c) == (PR-1, PC-1):
        answer = 'Voyager'
        send = start
        break
    if answer < result:
        answer = result
        send = start
    dx, dy = direction[d]
    if 0 <= r+dx < N and 0 <= c+dy < M:
        if matrix[r+dx][c+dy] == '.':
            queue.append((r+dx, c+dy, start, d, result+1))
        elif matrix[r+dx][c+dy] == '/':
            queue.append((r+dx, c+dy, start, slash[d], result+1))
        elif matrix[r+dx][c+dy] == '\\':
            queue.append((r+dx, c+dy, start, backslash[d], result+1))
print(send or 'U')
print(answer)