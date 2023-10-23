from sys import stdin
input = stdin.readline

def recur(n, start, p, f, s, v, c, arr):
    global mn, answer
    if p >= mp and f >= mf and s >= ms and v >= mv and c < mn:
        mn = min(mn, c)
        answer = arr
    if n >= N or c > mn: return

    for i in range(start, N):
        pp, ff, ss, vv, cc = A[i]
        recur(n+1, i+1, p+pp, f+ff, s+ss, v+vv, c+cc, arr+[i+1])

N = int(input())
mp, mf, ms, mv = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = None
mn = 987654321
recur(0, 0, 0, 0, 0, 0, 0, [])
if answer is None:
    print(-1)
else:
    print(mn)
    print(*answer)