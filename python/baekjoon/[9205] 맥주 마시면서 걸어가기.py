from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sr, sc = map(int, input().split())
    cvs = [list(map(int, input().split())) for _ in range(N)]
    er, ec = map(int, input().split())
    queue = deque([(sr, sc, 20)])
    V = [0]*N
    while queue:
        r, c, beer = queue.pop()
        distance = abs(er-r)+abs(ec-c)
        if distance <= beer*50:
            print('happy')
            break
        for i, (cr, cc) in enumerate(cvs):
            if V[i] or (r, c) == (cr, cc): continue
            elif abs(cr-r)+abs(cc-c) <= beer*50:
                V[i] = 1
                queue.append((cr, cc, 20))
    else: print('sad')