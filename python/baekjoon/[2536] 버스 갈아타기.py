import sys
input = sys.stdin.readline

def solve(queue, V):
    turn = 1
    while queue:
        next_q = []
        for x, y, xx, yy in queue:
            if x <= ex <= xx and y <= ey <= yy: return turn
            for b, (x1, y1, x2, y2) in enumerate(bus):
                if V[b]: continue
                if (x1 <= xx and x <= x2) and (y1 <= yy and y <= y2):
                    V[b] = 1
                    next_q.append((x1, y1, x2, y2))
        queue = next_q
        turn += 1

M, N = map(int, input().split())
K = int(input())
bus = [[] for _ in range(K)]
for idx in range(K):
    b, x1, y1, x2, y2 = map(int, input().split())
    bus[idx] = [min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)]
sx, sy, ex, ey = map(int, input().split())
queue = []
V = [0]*K
for b, (x1, y1, x2, y2) in enumerate(bus):
    if x1 <= sx <= x2 and y1 <= sy <= y2:
        V[b] = 1
        queue.append((x1, y1, x2, y2))
print(solve(queue, V))