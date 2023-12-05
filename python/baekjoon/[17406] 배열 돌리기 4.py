import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

def rotate(rr, cc, s, B):
    for i in range(s):
        lst = deque()
        for c in range(cc-s+i, cc+s-i+1):
            lst.append(B[rr-s+i-1][c-1])
        for r in range(rr-s+i+1, rr+s-i):
            lst.append(B[r-1][cc+s-i-1])
        for c in range(cc+s-i, cc-s+i, -1):
            lst.append(B[rr+s-i-1][c-1])
        for r in range(rr+s-i, rr-s+i, -1):
            lst.append(B[r-1][cc-s+i-1])
        lst.rotate(1)
        for c in range(cc-s+i, cc+s-i+1):
            B[rr-s+i-1][c-1] = lst.popleft()
        for r in range(rr-s+i+1, rr+s-i):
            B[r-1][cc+s-i-1] = lst.popleft()
        for c in range(cc+s-i, cc-s+i, -1):
            B[rr+s-i-1][c-1] = lst.popleft()
        for r in range(rr+s-i, rr-s+i, -1):
            B[r-1][cc-s+i-1] = lst.popleft()
    return B

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
perm = []
for _ in range(K):
    r, c, s = map(int, input().split())
    perm.append((r, c, s))
answer = 987654321
for p in permutations(perm, K):
    B = [row[:] for row in A]
    for r, c, s in p:
        B = rotate(r, c, s, B)
    answer = min(answer, min([sum(row) for row in B]))
print(answer)