import sys
input = sys.stdin.readline

def change(A):
    return ''.join(map(lambda x: ''.join(x), A))

def solve():
    queue = [(0, A)]
    while queue:
        next_q = []
        for cnt, arr in queue:
            if change(arr) == final: return cnt
            for r in range(4):
                for c in range(4):
                    if arr[r][c] == '1':
                        for dx, dy in ((2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)):
                            nx, ny = r + dx, c + dy
                            if 0 <= nx < 4 and 0 <= ny < 4:
                                arr[r][c], arr[nx][ny] = arr[nx][ny], arr[r][c]
                                state = change(arr)
                                if state not in V:
                                    V.add(state)
                                    next_q.append((cnt + 1, [row[:] for row in arr]))
                                arr[r][c], arr[nx][ny] = arr[nx][ny], arr[r][c]
        queue = next_q

A = [list(input().rstrip()) for _ in range(4)]
B = [list(input().rstrip()) for _ in range(4)]
V = set()
state, final = change(A), change(B)
V.add(state)
print(solve())